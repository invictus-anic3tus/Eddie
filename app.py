from flask import Flask, request, render_template, jsonify, send_from_directory
from flask_cors import CORS
from g4f.client import Client

app = Flask(__name__)
CORS(app)

@app.route('/')
def serve_html():
    return send_from_directory('', 'index.html')

def ai(message):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],
        # Add any other necessary parameters
    )
    return response.choices[0].message.content


@app.route('/submit', methods=['POST'])
def handle_submit():
    data = request.get_json()
    user_message = data.get('message', '')
    response_message = ai(user_message)
    return response_message



