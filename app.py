__author__ = 'Adamlieberman'
from flask import Flask, render_template, request
from scraper import scrape_icd9, scrape_icd92, cliner_response
import os;
import requests;
import json;
import sys;

from feature_generation import *
from LSTM_handler import *

app = Flask(__name__)

@app.route('/')
def input_page():
    requests.get('http://doctorann-api.herokuapp.com/api/wake');
    return render_template('main.html')

@app.route('/results.html')
def results_page():
    return render_template('results.html')

@app.route('/',methods=['GET','POST'])
def input_page_post():

    #Obtain the user's clinical note
    clinical_note = request.form.get('clinical_note',type=str)

    #Conditional Random Field  on user's clinical note to obtain labeling
    cliner_note = cliner_response(clinical_note)

    #Create feature vector
    #feature = create_feature(clinical_note)


    r = requests.post('http://doctorann-api.herokuapp.com/api/transform', json={'note' : str(cliner_note)});
    tx = r.text;

    feature = np.array(json.loads(str(tx))['result']);

    #Load the LSTM
    model = load_LSTM()

    #Return the ICD9 codes, probabilities, and topk
    codes, probabilities, topk = predict(feature,model,3)

    format_probs = []
    for i in probabilities:
        format_probs.append(str(i*100)+" %")


    #Scrape the codes descriptions
    description = scrape_icd92(codes)

    return render_template('results.html',note=cliner_note, code=codes,description=description,format_probs=format_probs)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000));
    app.run(host='0.0.0.0', port=port, debug=True);