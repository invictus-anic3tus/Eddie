from flask import Flask, render_template, request, jsonify

from g4f.client import Client

app = Flask(__name__)

@app.route('/run-script', methods=['GET'])
def run_script():
    text = entry.get()
    client = Client()
    global response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}],
        # Add any other necessary parameters
    )
    
    result = response.choices[0].message.content
    return jsonify({"message": result})

if __name__ == "__main__":
    app.run()