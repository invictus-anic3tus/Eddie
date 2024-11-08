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




from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/run-script', methods=['GET'])
def run_script():
    # Replace this with the script you want to run
    result = "Script has run successfully!"
    return jsonify({"message": result})  # Ensures JSON response
