from flask import Flask, jsonify, request

import joblib
import pandas as pd
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
     json_ = request.json
     print(json_)
     query_df = pd.DataFrame(json_ ,index = [1])
     #pipe= getpipline()

 
     
     #query = pd.get_dummies(query_df)
     prediction = pipe.predict(query_df)
     return jsonify({'prediction': list(prediction)})

if __name__ == '__main__':
     pipe = joblib.load('LinearRegressionModel.pkl')
     app.run(port=8080)