import pytest
import project

def test_writecsv():
     assert project.write_csv("good","Great")==True
     assert project.write_csv("hello","Hello there,how can i assist you today!")==True
     assert project.write_csv("clear","ok")==True


def test_readcsv():
     assert project.read_csv("good") == "Great"
     assert project.read_csv("hello") == "Hello there,how can i assist you today!"
     assert project.read_csv("clear")=="ok"


def test_chatbot(monkeypatch):
    inputs = iter(["good", "unknown_question", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    responses = []
    monkeypatch.setattr('builtins.print', lambda msg: responses.append(msg))

    project.chatbot()

    assert "🤖 Chatbot: Great" in responses
    assert "🤖 Chatbot: I do not know the answer. What should I reply next time?" in responses
