from g4f.client import Client

from flask import Flask, render_template, request, jsonify

import tkinter as tk

app = Flask(__name__)

# # Create main window
# window = tk.Tk()
# window.title("Text Input Example")

# # Create a label
# label = tk.Label(window, text="Enter your name:")
# label.pack()

# # Create a text entry box
# entry = tk.Entry(window)
# entry.pack()


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
    

# print(message + "Gooba gooba gooba")

# button = tk.Button(window, text="Submit", command=submit)
# button.pack()

# Start the GUI
# window.mainloop()

