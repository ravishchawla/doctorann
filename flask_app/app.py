__author__ = 'Adamlieberman'
from flask import Flask, render_template, request
from scraper import scrape_icd9
app = Flask(__name__)

@app.route('/')
def input_page():
    return render_template('main.html')

@app.route('/results.html')
def results_page():
    return render_template('results.html')

@app.route('/',methods=['GET','POST'])
def input_page_post():

    #Obtain the clinical note
    clinical_note = request.form.get('clinical_note',type=str)
    codes = [250.01, 250.02, 250.03]
    description = scrape_icd9(codes)
    #Process the clinical note
    clinical_note = clinical_note.lower()
    t = 'h<font color="red">aaaa</font>gggg'
    return render_template('results.html',note=clinical_note, code=codes,t=t,description=description)


if __name__ == "__main__":
    app.run(debug=True)