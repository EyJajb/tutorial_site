import projects #projects definitions are placed in different file
#import data
# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
name = form.getvalue('name')
email = form.getvalue('email')
class1 = form.getvalue('class 1')
class2 = form.getvalue('class 2')
class3 = form.getvalue('class 3')

# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

@app.route('/')
def home_route():
    return render_template("home.html", projects=projects.setup())
@app.route('/test/')
def test_route():
    return render_template("test.html", projects=projects.setup())





if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True)
