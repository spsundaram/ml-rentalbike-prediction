import pandas as pd
import os
import numpy as np
import joblib
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
port = int(os.getenv('PORT',5600))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/rentalp',methods=['POST'])
def rentalp():
    if request.method == 'POST':
        try:
            post_data = request.get_json()
            #json_data = json.dumps(post_data)
            #data = json.load(json_data)
            data = post_data
            # Store JSON data in a list
            data_list = [data[key] for key in data]
            filename = 'bike-share.pkl'
            loaded_model = joblib.load(filename)
            X_new = np.array([data_list]).astype('float64')
            # Use the model to predict tomorrow's rentals
            result = loaded_model.predict(X_new)
            return str(np.round(result[0]))

        except Exception as e:
            return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=port,debug=True)