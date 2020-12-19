#import projects #projects definitions are placed in different file
#import data

#import data

# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

@app.route('/')
def home_route():
    return render_template("home.html")


if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True)
