__author__ = 'Adamlieberman'
import numpy as np
import pickle
import keras.backend as K
from keras.models import Sequential
from keras.layers import Dense, Activation, Reshape
from keras.layers import LSTM

from sklearn.cross_validation import train_test_split
from keras.models import load_model   #save_model requires h5py, need to pip install h5py

def load_LSTM():
    '''
    Loads the LSTM model and use the custom multiclass_loss function as the loss
    '''
    return load_model('khot_LSTM.h5', custom_objects={"multiclass_loss":multiclass_loss})


def predict(row,model,k):
    '''
    Obtain predictions for user's clinical note
    Returns the top k predicted ICD-9 codes, their indices in the probability matrix, and the top k
    probabilities.
    '''
    row = row.reshape(1,1,1000)
    pred = model.predict(row)[0][0]


    topk = pred.argsort()[-k:][::-1]            #The indices of the topk probabilities
    probabilities = pred[topk]                  #The probabilities of the topk indices


    #load pickled dictioanry, flip the key and value, and then find the key that matches the value
    #return the list of ICD9 codes

    with open(r"icd9_mapping", "rb") as input_file:
        icd_dict = pickle.load(input_file)

    flipped_icd_dict =  {v: k for k, v in icd_dict.iteritems()}
    ls_ICD9 = [flipped_icd_dict[i] for i in topk]
    return ls_ICD9, probabilities, topk



def multiclass_loss(y_true, y_pred):
    '''
    Our custom multiclass loss function
    '''
    EPS = 1e-5
    y_pred = K.clip(y_pred, EPS, 1 - EPS)
    return -K.mean((1 - y_true) * K.log(1 - y_pred) + y_true * K.log(y_pred))

def run_all():
    model = load_LSTM()
    ls_ICD9, probabilities, topk = predict()


if __name__ == "__main__":
    with open(r"icd9_mapping", "rb") as input_file:
        dict_icd9_index = pickle.load(input_file)
    print(dict_icd9_index)
    #mode = load_LSTM()