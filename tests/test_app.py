from app import chatbot_response

def test_hello():
    assert chatbot_response("hello") == "Hi there! How can I help you?"

def test_bye():
    assert chatbot_response("bye") == "Goodbye! Have a great day!"

def test_unknown():
    assert "not sure" in chatbot_response("random text")
