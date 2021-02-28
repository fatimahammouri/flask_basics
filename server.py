"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.</html>
              For a special hello <a href="/hello" > click here </a>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
        <div>
          <label>What's your name?</label>
          <input type="text" name="person">

          </div>

          <div>
          <label>Choose your favourite compliment:</label>
            <div>
            <select name="compliment">
              <option name ="compliment" >fantastic</option>
              <option name ="compliment" >smashing</option>
              <option name ="compliment" >Amazing</option>
              <option name ="compliment" >incredible</option>
            </select>
            </div>
          </div>

          <div>
            <label>What do you enjoy doing ?</label>
          <input type="text" name="hobby">
          </div>

          <div>
          <input type="submit" value="Submit">
          </div>
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    # compliment = choice(AWESOMENESS)
    compliment = request.args.get("compliment")

    hobby = request.args.get("hobby")
    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {} at {}!
      </body>
    </html>
    """.format(player, compliment, hobby)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
