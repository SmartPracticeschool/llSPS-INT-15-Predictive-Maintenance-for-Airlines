# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:18:11 2020

@author: prads
"""

from flask import Flask,render_template,request

import pickle
import numpy as np

model = pickle.load(open('profit.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login',methods =['POST'])
def login():
    ms = request.form['ms']
    ad = request.form['as']
    rd = request.form['rd']
    s = request.form['s']
    if(s == "Newyork"):
        s1,s2,s3 = 0,0,1
    if(s == "California"):
        s1,s2,s3 = 1,0,0
    if(s == "Florida"):
        s1,s2,s3 = 0,1,0
        
    total = [[s1,s2,s3,int(rd),int(ad),int(ms)]]
    print(total)
    y_pred = model.predict(total)
    
    print(y_pred)
    
    
    return render_template("index.html",showcase = "the profit that you would get is "+ str(y_pred[0][0]))
    


if __name__ == '__main__':
    app.run(debug = True)



