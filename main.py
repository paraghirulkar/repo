
from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)
pkl_imprt = open('bank_note_base.pkl','rb')
classifier = pickle.load(pkl_imprt)

@app.route('/')
def base():
    return "Base path or welcome page"

@app.route('/authenticate')  
def authenticate_note():
    varaince = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    # test = pd.read_csv(request.files.get("file"))
    return f"""My predicted value is {classifier.predict([[varaince,skewness,curtosis,entropy]])}"""


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
