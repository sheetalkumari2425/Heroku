# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 01:28:01 2022

@author: teladmin
"""

import numpy as np
from flask import Flask, jsonify, render_template
import pickle
from flask import request

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering returns on HTML GUI

    '''
    
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    output = round(prediction[0], 2)
    
    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))




if __name__=="__main__":
    app.run(debug=True)