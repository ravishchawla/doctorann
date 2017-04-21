__author__ = 'Adamlieberman'
import numpy as np

import keras.backend as K
from keras.models import Sequential
from keras.layers import Dense, Activation, Reshape
from keras.layers import LSTM

from sklearn.cross_validation import train_test_split
from keras.models import load_model   #save_model requires h5py, need to pip install h5py

def load_LSTM():
    return load_model('khot_LSTM.h5', custom_objects={"multiclass_loss":multiclass_loss})


def predict(row,model,k):
    pred = model.predict(row)
    topk = pred.argsort()[-k:][::-k]
    #load pickled dictioanry and then find the key that matches the value
    #return the list of ICD9 codes

#Our custom loss function
def multiclass_loss(y_true, y_pred):
    EPS = 1e-5
    y_pred = K.clip(y_pred, EPS, 1 - EPS)
    return -K.mean((1 - y_true) * K.log(1 - y_pred) + y_true * K.log(y_pred))



if __name__ == "__main__":
    mode = load_LSTM()