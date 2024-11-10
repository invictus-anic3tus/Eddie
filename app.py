# from g4f.client import Client

# from flask import Flask, render_template, request, jsonify

# app = Flask(__name__)


# @app.route('/run-script', methods=['GET'])
# # Create a button to submit the input
# def run_script():
#     client = Client()
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": "Wassup"}],
#         # Add any other necessary parameters
#     )
#     return jsonify({"message": response})

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def serve_html():
    return send_from_directory('', 'index.html')

@app.route('/submit', methods=['POST'])
def handle_submit():
    data = request.get_json()
    user_message = data.get('message', '')
    response_message = f"You submitted: {user_message}"
    return response_message


