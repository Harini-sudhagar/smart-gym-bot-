from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import hashlib
import nltk
nltk.download('omw-1.4')
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings("ignore")
app = Flask(__name__)
app.secret_key = "your_secret_key"  # Secret key for session management
# Download NLTK data
nltk.download("punkt")
nltk.download("wordnet")
# Read dataset
with open("data.txt", "r", encoding="utf-8") as f:
    raw_lines = f.readlines()
# Associate each question-answer pair with an image
images = [f"static/images/image{i + 1}.jpg" for i in range(6)]
responses = []
for i, line in enumerate(raw_lines):
    if line.strip() and "|" in line:
        question, answer = line.strip().split("|", 1)
        img = images[i % len(images)]  # Assign images cyclically
        responses.append({"question": question.strip(), "answer": answer.strip(), "image": img})
# NLP preprocessing
lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
def LemNormalize(text):
    remove_punct_dict = dict((ord(punct), None) for punct in "!@#$%^&*()[]{};:,./<>?")
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
def get_response(user_input):
    user_input = user_input.lower()
    corpus = [resp["question"] for resp in responses]  # Only compare questions
    corpus.append(user_input)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words="english")
    tfidf = TfidfVec.fit_transform(corpus)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        return {"text": "I'm sorry, I didn't understand that.", "image": ""}
    else:
        matched_response = responses[idx]
        return {"text": matched_response["answer"], "image": matched_response["image"]}
@app.route("/")
def index():
    if "username" in session:
        return render_template("index.html")
    return redirect(url_for("login"))
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        # Dummy user credentials
        if username == "admin" and hashed_password == hashlib.md5("1234".encode()).hexdigest():
            session["username"] = username
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Invalid username or password")
 return render_template("login.html")
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))
@app.route("/get_response", methods=["POST"])
def chat_response():
    user_input = request.form.get("user_input")
    bot_response = get_response(user_input)
    return jsonify(bot_response)
if __name__ == "__main__":
    app.run(debug=False)
