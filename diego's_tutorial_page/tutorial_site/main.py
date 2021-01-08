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
from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
import os
#create a Flask instance
app = Flask(__name__)

@app.route('/')
def home_route():
    return render_template("home.html", projects=projects.setup())
@app.route('/test/')
def test_route():
    return render_template("test.html", projects=projects.setup())

@app.route('/calc/')
def calc_route():
    return render_template("APCalcAB.html", projects=projects.setup())
@app.route('/phys/')
def phys_route():
    return render_template("APPhysicsC.html", projects=projects.setup())
@app.route('/euro/')
def euro_route():
    return render_template("APEuro.html", projects=projects.setup())
@app.route('/hist/')
def hist_route():
    return render_template("APEuro.html", projects=projects.setup())
@app.route('/precalc/')
def precalc_route():
    return render_template("APEuro.html", projects=projects.setup())

@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'GET':
        return render_template("form.html")
    elif request.method == 'POST':
        if request.form.get('title') != '' and request.form.get('category') != '' and request.form.get('description') != '' :
            title = request.form.get('title')
            category = request.form.get('category')
            description = request.form.get('description')
            return redirect("/showform?title=" + str(title) +"&category=" + str(category) + "&description=" + str(description) + "&video=" + str(video), code=302)
        else:
            return render_template("form.html")

@app.route('/showform', methods=['POST', 'GET'])
def showform():
    title = request.args.get('title')
    category = request.args.get('category')
    description = request.args.get('description')
    return render_template("showform.html", title=title , description=description , category=category)




if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True)
