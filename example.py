from g4f.client import Client

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

message = ""

# Create a button to submit the input
def submit():
    text = entry.get()
    client = Client()
    global response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}],
        # Add any other necessary parameters
    )
    global message
    message = response.choices[0].message.content
    print(message)
