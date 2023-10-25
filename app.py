from keras.models import load_model
from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

# Load the model
model = load_model("credit_card_fraud_model.h5")

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from POST request
    data = request.get_json(force=True)
    
    # Convert data to numpy array and predict
    prediction = model.predict(np.array([data['features']]))
    
    # Convert prediction to binary label
    label = (prediction > 0.5).astype(int)
    
    # Send back to the client
    return jsonify(int(label[0][0]))

if __name__ == '__main__':
    app.run(port=5000, debug=True)

