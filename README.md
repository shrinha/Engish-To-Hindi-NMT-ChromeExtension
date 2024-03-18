# Engish-To-Hindi-NMT-ChromeExtension
An English to Hindi Neural Machine Translator Model Deployable as a Chrome Extension on your browsers.

# Installation & Set Up
### 1) Clone/ Download the Eng2Hin Project Folder to your local computer.

### 2) Download The Trained Model  
Since Github Limits the upload size for files, the trained model must be downloaded from the following link and pasted into the model directory inside Eng2Hin: https://drive.google.com/file/d/1vAjF6q5VV-zLr8nsfjcfcmDN8LWTYrrE/view?usp=sharing. 
Moreover, If you wish to refer to the training/tuning of the model, I've added the colab notebook

### 3) Install the Prerequisite Libraries (Copy to the Command Line or Terminal)
* Tensorflow

      pip install tensorflow
* Flask

      pip install Flask
* Flask-CORS

      pip install Flask-CORS
* Transformers Library and Numpy

      pip install numpy transformers
* Additionally, ensure that you have Python installed for running app.py (and pip if you intend to use the above commands)

### 4) Load the Eng2Hin Folder as Extension in your Chrome browser
* Go to the Extensions page by entering chrome://extensions in a new tab. (By design chrome:// URLs are not linkable). Alternatively, click the Extensions menu puzzle button and select Manage Extensions at the bottom of the menu.
* Enable Developer Mode by clicking the toggle switch next to Developer Mode.
* Click the Load unpacked button and select the extension directory (Eng2Hin)

### 5) Run the Backend Server that will do the Translation
* Conventionally, the server is hosted over a 3rd Party Website, and the extension makes an API call to send the input text and receive the result. However, This is done locally in our case. I've provided an app.py file, which basically acts as a backend server for running the model using the input text provided via the script files.
  
* To do so, Go to the project directory and run app.py using the following command

        python app.py


### 6) Click on the Extensions button on your browser to open the Extension whenever you wish to translate any text
Note: In some cases, generating the translation on the first try might take some time since some resources (such as the tokenizer) are loaded onto the server.

      


      
   


   
   

   
