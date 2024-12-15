from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load('./model/model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        df = pd.DataFrame([data])
        prediction = model.predict(df)[0]
        print(prediction)
        return jsonify({"predicted dollar cost": prediction}), 200
    except Exception as e:
        return jsonify({"error": e}), 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')