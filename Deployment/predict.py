import numpy as np
from flask import Flask
from flask import request
from flask import jsonify
import pickle

with open('tree.bin','rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('student')

@app.route('/predict', methods=['POST'])
def predict():

    student = request.get_json()

    X = dv.transform([student])
    y_pred = model.predict_proba(X)[0, 1]
    keep_scholarship = y_pred >= 0.5

    result = {
        'keep_scholarship_probability': float(y_pred),
        'keep_scholarship': bool(keep_scholarship) 
    }

    return jsonify(result)


if __name__ == "__main__":

    app.run(debug=True, host='0.0.0.0', port=9696)