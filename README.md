#  Dr. ANN

<img src='http://i.imgur.com/bE6iAGu.jpg' width=100x/> 

## [https://www.doctorann.xyz](https://www.doctorann.xyz)


A web based system that uses deep learning to diagnosis patients based on their clinical notes.

### Authors - Ravish Chawla, Adam Lieberman, Garrett, Mallory

## Front-End code.

#### Python Files

- app.py
  - This file instantiates the Flask App and controls the necessary HTTP routes.
- scraper.py
  - This script scrapes the ICD9 code descriptions for the predicted ICD9 codes.  
- feature_generation.py
  - This Class generates the features from the given Clinical Note.
- LSTM_Handler.py
  - This Class loads the LSTM model and predicts the ICD9 codes from the features generated in feature_generation.py.

#### Flask Files

- static/
  - This folder contains static files, such as JS, CSS, and Image files.
- templates/
  - This folder contains the HTML template files.

#### Heroku Files

- Procfile
  - This script tells Heroku which file to run and how.
- requirements.txt
  - This file tells Heroku which packages to install.

#### Saved Objects and Models

- cleaned_tfidf_vectorizer_fit
  - This model stores the trained TfIdf vectorizer model.
- khot_LSTM.h5
  - This is a Trained Neural Network model on 32 Neurons. It is used for prediction in this app.
- khot_LSTM_1353.h5
  - This is an alternate model, also trained on 32 Neurons, but not used for final app.

#### Doctor ANN API

The code for the Doctor ANN API is not located on Github, but on Heroku because of stricter file-size limitations on Github. That code can be obtained by Cloning the Heroku repository into your local machine. Furthermore, we suggest that you obtain both the Front-End code and the API code from Heroku, instead of downloading them from here. Here are the instructions to obtain the code:

1. Request access to the DoctorANN and DoctorANN-api Heroku apps by emailing at: [ravishchawla@gmail.com](mailto:ravishchawla@gmail.com). Because of how permissions work on Heroku, we cannot make the app public, so you must be added to the apps before cloning them.

2. Perform the following GIT commands:
   - `cd <workspace>`
   - `mkdir -p doctorann && mkdir -p doctorann-api`
   - `cd doctorann`
   - `git clone https://git.heroku.com/doctorann.git`
   - `cd ../doctorann-api`
   - `git clone https://git.heroku.com/doctorann-api.git`

## To run the Code

Please first install the requirements in requirements.txt. These can all be installed with pip. We used python 2.7.13 for this project. Navigate to the doctorann-api repository and change the port from 5000 to 5001 in app.py. Next, navigate to the Dr-ANN repository and run app.py. Go to port 5000 in your local host and the web application will be loaded.

Using the above directory structure and port assignments, run the following instructions in order:

- `cd <workspace>`
- `cd doctorann`
- `python2.7 app.py &`
- `cd ../doctorann-api`
- `python2.7 app.py`

<img src='http://i.imgur.com/bE6iAGu.jpg' width=800px/>
