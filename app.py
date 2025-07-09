from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Load model
MODEL_PATH = "suicide_risk_model.pkl"
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    model = None

@app.route('/')
def home():
    if not model:
        return "❌ Model file not found. Make sure 'suicide_risk_model.pkl' is in the same folder."
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return "❌ Model file not found."

    depression = request.form.get('depression')
    anxiety = request.form.get('anxiety')
    panic = request.form.get('panic')
    treatment = request.form.get('treatment')

    input_vector = [
        1 if depression == "Yes" else 0,
        1 if anxiety == "Yes" else 0,
        1 if panic == "Yes" else 0,
        1 if treatment == "Yes" else 0,
    ]

    prediction = model.predict([input_vector])[0]

    if prediction == 1:
        message = "⚠️ This student may be at risk. Please refer them to mental health support."
        status = "risk"
    else:
        message = "✅ This student is not currently flagged as high risk."
        status = "safe"

    return render_template('index.html', prediction=message, status=status)

if __name__ == '__main__':
    app.run(debug=True)
