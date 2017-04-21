__author__ = 'Adamlieberman'
import re;

import pandas as pd;

from sklearn.externals import joblib;

from LSTM_handler import *

def get_stopwords():
    '''Removes the stop words'''
    stop_words = str();
    with open('nltk', 'r') as f:
        for line in f:
            stop_words = stop_words + '\\b' + line.strip() + '\\b' + '|';
    stop_words = stop_words[0:-1];
    return stop_words


def clean_text(notes_df):
    '''
    Cleanes the user's clinical note
    '''
    stop_words = get_stopwords();
    notes_filtered = notes_df['TEXT'].apply(lambda row: re.sub("21[0-9]{2}.[0-1]?[0-9]{1}.[0-3]?[0-9]{1}.+[0-2]{1}[0-9]{1}:[0-5]{1}[0-9]{1}.+[\bAM\b|\bPM\b]", " ", row));
    notes_filtered = notes_filtered.apply(lambda row: re.sub("[^a-zA-Z0-9\.]", " ", row.lower()));
    notes_nostops = notes_filtered.apply(lambda row: re.sub(stop_words, ' ', row));
    notes_final = notes_nostops.apply(lambda row: " ".join(row.split()));
    notes_df = notes_df.drop('TEXT', axis=1);
    notes_df = notes_df.assign(TEXT = notes_final.values)
    return notes_df




def create_feature(note):

    #Add user's clinical note as a single item in pandas dataframe
    note = [note]
    df = pd.DataFrame()
    df["TEXT"] = note

    #Clean user's clinical note
    df_cleaned_note = clean_text(df)
    cleaned_note = df_cleaned_note["TEXT"].values

    #Unpickel the Counte Vectorizer Model
    cleaned_tfidf_vectorizer = joblib.load("cleaned_tfidf_vectorizer_fit")
    cleaned_tfidf_counts = cleaned_tfidf_vectorizer.transform(cleaned_note)

    #Load SVD
    svd = joblib.load("saved_fit_svd/fit_svd_420_morning")
    feature = svd.transform(cleaned_tfidf_counts)

    return feature



if __name__ == "__main__":
    note = "The patient fell and hurt his shoulder. He was prescribed advil and is scheduled for a check up next week."
    #df = pd.DataFrame()
    #df["TEXT"] = note
    feature = create_feature(note)


    model = load_LSTM()
    ls_ICD9, probabilities, topk = predict(feature,model,3)

    print ls_ICD9

