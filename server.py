from flask import Flask
import random

app = Flask(__name__)
number = random.randint(0, 9)

@app.route('/')
def Homepage():
    return '<h1> Guess a number between 0 and 9 </h1>' \
           '<img src="https://media3.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif?cid=ecf05e47e847iy765158lpx3nmq901w00u51jci5rmwkcswe&rid=giphy.gif&ct=g" width="480" height="480" frameBorder="0" class="giphy-embed">'


@app.route('/<int:guess>')
def random_number(guess):
    if guess == number:
        return '<h1 style="color:green"> You found me </h1>' \
               '<img src="https://media3.giphy.com/media/UAXK9VGoJTbdcPgmcJ/giphy.gif?cid=ecf05e47dj77vxzeak4q9ytz70pozyg211tf6bxppmmv5qp8&rid=giphy.gif&ct=g">'
    elif guess < number:
        return '<h1 style="color:red"> Too Low, Guess again </h1>' \
               '<img src="https://media4.giphy.com/media/YiKiqMTzrQZwmF4I5N/giphy.gif?cid=ecf05e47h1936rq95l336wd1pdcxhxjo4ei3b9trmyky8vl0&rid=giphy.gif&ct=g">'
    elif guess > number:
        return '<h1 style="color:purple"> Too High, Guess again </h1>' \
               '<img src="https://media2.giphy.com/media/L422JoNlBBBD42zkQ9/giphy.gif?cid=ecf05e47ia20p61sxuqd89wolxjxhjh9obpspullrgq7rmoy&rid=giphy.gif&ct=g">'


if __name__ == '__main__':
    app.run(debug=True)
