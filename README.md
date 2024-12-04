1. Open the official website [python.org](https://www.python.org) and download Python version 3.6.5 executable installer. This version is required because the package versions and the Python version must be compatible to run your program.

2. After installation, open the Command Prompt and execute the following commands step by step:  

   - Type python -m pip install --upgrade pip --user and press Enter.  
   - Type pip install chatterbot --user and press Enter.  
   - Type pip install nltk --user and press Enter.  
   - Type pip install pyttsx3 --user (for Python text-to-speech conversion) and press Enter.  
   - Type pip install flask --user (a framework for Python web applications) and press Enter.  

3. Once these installations are complete, go to Drive where you have saved your project folder and open the folder named Project. (This program can be run in Visual Studio, but make sure your system is running Python version 3.6.5.)  

4. To check the Python version, open the Command Prompt, type python, and press Enter. If a different version is displayed, you need to change it to version 3.6.5.  

5. To change the Python version:  
   - Edit the system environment variables.  
   - Click Environment Variables, then navigate to Path, and update it to point to Python version 3.6.5.  

6. In the Project folder on Drive , you will find the following files:  
   - flask1 (default file)  
   - static (contains images for output in JPEG format)  
   - style (an HTML file)  
   - templates (contains HTML code)  
   - data (includes datasets like questions and answers related to your project)  
   - img (contains your project code)  

7. Right-click the img file and select Edit with IDLE (Python version 3.6.5).  

8. In the coding page that opens, run the program. Once the program runs, copy the website link shown in the output and paste it into a browser.  

9. The browser will display the login page for your chatbot. Enter the User ID and Password  to access the main page.  

10. You can now ask questions either through text or voice. The chatbot will respond in both text and voice, along with a related image.
