from flask import Flask, render_template, request, jsonify
from app.chatbot import Chatbot

app = Flask(__name__)
chatbot = Chatbot()  # Initialize your chatbot class

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get('message')
    bot_response = chatbot.get_response(user_message)  # Assuming you have a method to get chatbot response
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)
