import pickle

from flask import Flask
from flask import request
from flask import jsonify
from  pandas import DataFrame

model_file = 'model.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

app = Flask('potability')

@app.route('/predict', methods=['POST'])
def predict():
    parameters = request.get_json() # return a dict

    X = DataFrame.from_dict([parameters])
    y_pred = model.predict_proba(X)[0, 1]

    result = {
        "payload": parameters,
        "potable_probability": float(y_pred)
    }

    return jsonify(result)
    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)