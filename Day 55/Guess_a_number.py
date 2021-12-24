from flask import Flask
import random

app = Flask(__name__)

random_no = random.randint(1, 9)


@app.route("/")
def hello_world():
    return '<h1>Guess a Number between 0 and 9 <h1>' \
        '<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>'


@app.route("/bye")
def bye():
    return "Bye"


@app.route("/<int:guess>")
def guess(guess):
    if guess > random_no:
        return "<h1 style='color:red'>Too High<h1>" \
            "<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>"
    elif guess < random_no:
        return "<h1 style='color:blue'>Too Low<h1>" \
            "<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>"
    else:
        return "<h1 style='color:green'>You Got it!<h1>" \
            "<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>"


if __name__ == "__main__":
    app.run(debug=True)
