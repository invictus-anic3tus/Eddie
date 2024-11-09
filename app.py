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

from flask import Flask, send_from_directory

app = Flask(__name__)

# Route to serve the HTML file
@app.route('/')
def serve_html():
    return send_from_directory('', 'index.html')

# Route to handle the button click and send the message
@app.route('/message')
def get_message():
    return "Hello from the Vercel app!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

