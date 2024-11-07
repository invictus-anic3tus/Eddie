from flask import Flask, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Define a route (URL endpoint) for your Python function
@app.route('/')
def home():
    return "Welcome to my Python script!"

# Define a route for executing your Python script's functionality
@app.route('/run-script', methods=['POST'])
def run_script():
    # Example function that represents your Python script
    def my_script():
        # Add the main code of your Python script here
        result = "Hello from my script!"  # Replace this with your actual script's output
        return result

    # Run your script and return the result
    result = my_script()
    return jsonify({"result": result})

# Run the app if this file is run directly
if __name__ == '__main__':
    app.run(debug=True)