#  Dr. ANN

<img src='http://i.imgur.com/bE6iAGu.jpg' width=100x/> 

## [https://www.doctorann.xyz](https://www.doctorann.xyz)


A web based system that uses deep learning to diagnosis patients based on their clinical notes.

###Authors - Ravish Chawla, Adam Lieberman, Garrett, Mallory

## Front-End code.

#### Python Files

- app.py
	- This file instantiates the Flask App and controls the necessary HTTP routes.
- scraper.py
	- This script scrapes the ICD9 
- feature_generation.py
	- This Class generates the features from the given Clinical Note.
- LSTM_Handler.py
	- This Class predicts the features from the features in the previous step.

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




## To run the Code

You can run the Site, you can run App.py. However, because of file size limitatins, the SVD model was not uploaded to Git. This means that the model must be obtained again using the Feature Construction code in the base repository.


<img src='http://i.imgur.com/bE6iAGu.jpg' width=800px/>
