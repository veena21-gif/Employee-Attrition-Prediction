from flask import Flask, request, jsonify
import joblib, os, numpy as np

app = Flask(__name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'attrition_model.pkl')
model = None
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    print('Model load error (run training first):', e)

@app.route('/')
def hello():
    return 'Employee Attrition Prediction API running.'

@app.route('/predict', methods=['POST'])
def predict():
    payload = request.json
    # expected: feature vector as list or dict of values
    if isinstance(payload.get('features'), list):
        arr = np.array(payload['features']).reshape(1, -1)
    elif isinstance(payload.get('features'), dict):
        # assume ordered dict matching training columns
        arr = np.array(list(payload['features'].values())).reshape(1, -1)
    else:
        return jsonify({'error':'Invalid features format'}), 400

    if model is None:
        return jsonify({'error':'Model not available. Train model first.'}), 500

    prob = float(model.predict_proba(arr)[0][1]) if hasattr(model, 'predict_proba') else None
    pred = int(model.predict(arr)[0])
    return jsonify({'attrition_probability': prob, 'likely_to_leave': pred})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
