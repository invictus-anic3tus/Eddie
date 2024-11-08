from g4f.client import Client

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Create a button to submit the input
def submit():
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Wassup"}],
        # Add any other necessary parameters
    )
    return jsonify({"message": response})
