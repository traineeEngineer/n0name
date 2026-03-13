from flask import Flask, request, jsonify

app = Flask(__name__)

def chatbot_response(message):
    message = message.lower()
    if "hello" in message:
        return "Hi there! How can I help you?"
    elif "bye" in message:
        return "Goodbye! Have a great day!"
    elif "how are you" in message:
        return "I'm doing great, thanks for asking!"
    else:
        return "I'm not sure how to respond to that."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    response = chatbot_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
