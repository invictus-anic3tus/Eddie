from flask import Flask, request, render_template, jsonify, send_from_directory
from flask_cors import CORS
from g4f.client import Client

app = Flask(__name__)
CORS(app, resources={r"/submit": {"origins": r"^https://.*\.vercel\.app$"}})

@app.route('/')
def serve_html():
    return send_from_directory('', 'index.html')

prevmessages = [
    {"role": "system", "content": "You are an extremely optimistic and annoying AI bot who uses way too many exclamation points and question marks. Your name is Eddie. Also, please present any text styling in HTML format."}
]

def ai(message):

    prevmessages.append({"role": "user", "content": message})

    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=prevmessages,
        # Add any other necessary parameters
    )
    
    assistant_response = response['choices'][0]['message']['content']
    prevmessages.append({"role": "assistant", "content": assistant_response})

    return assistant_response


@app.route('/submit', methods=['POST'])
def handle_submit():
    data = request.get_json()
    user_message = data.get('message', '')
    response_message = ai(user_message)

    return jsonify({"response": response_message})

if __name__ == '__main__':
    app.run(debug=True)



