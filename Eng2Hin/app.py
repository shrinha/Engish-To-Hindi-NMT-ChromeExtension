from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
from flask_cors import CORS
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM
import tensorflow as tf
import os


app = Flask(__name__)
CORS(app)

model_checkpoint = "./model/"
model_tokenizor= "./model_tokenizor/"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_tokenizor)
model = TFAutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)



@app.route('/predict', methods=['POST'])
def predict():
    text = request.json.get('text')
    if text is not None:
        # Tokenize input text
        tokenized = tokenizer([text], return_tensors='tf', padding=True, truncation=True)
        
        # Generate output
        out = model.generate(tokenized.input_ids)
        
        # Decode output tokens
        prediction = tokenizer.decode(out[0], skip_special_tokens=True)

        
        return jsonify({'prediction': prediction})
    else:
        return jsonify({'error': 'Input text not provided.'})

if __name__ == '__main__':
    app.run(debug=True)