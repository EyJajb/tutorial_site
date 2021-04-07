#import data
# Import modules for CGI handling
import cgi, cgitb
import mysql.connector
from transfer import encode
from data import *

@@ -11,7 +10,6 @@

from __init__ import restapi_bp
from flask import render_template
import requests


# https://flask.palletsprojects.com/en/1.1.x/api/
@@ -22,50 +20,20 @@



mydb = mysql.connector.connect(
  host="localhost",
  user="tutoruser",
  password="eyjajb1234",
  database="tutordb"
)

def function(c, u, p):
     mycursor = mydb.cursor()
     sql = "INSERT INTO students (classes, username, password) VALUES (%s, %s, %s)"
     val = (c,u,p)
     mycursor.execute(sql, val)
     mydb.commit()

def binary(g):
    if g:
        return 1
    else:
        return 0

@app.route('/')
def home_route():
    return render_template("home.html", projects=projects.setup())
    #if not session.get('logged_in'):
     #   return render_template('login.html')
    #   return render_template('login.html')
    #else:
     #   return render_template("home.html", projects=projects.setup())
    #   return render_template("home.html", projects=projects.setup())
@app.route('/test/')
def test_route():
    return render_template("test.html", projects=projects.setup())
#, username=request.form['username'], password=request.form['password']

@app.route('/login', methods=['POST', 'GET'])
def do_admin_login():
     mycursor = mydb.cursor()
     mycursor.execute("SELECT * FROM students")
     myresult = mycursor.fetchall()
     # for x in myresult:
        #  print(x)
     if request.method == 'POST':
	     return render_template('login.html', a=function(encode(binary(request.form.get('1')),binary(request.form.get('2')),binary(request.form.get('3')),binary(request.form.get('4')),binary(request.form.get('5')),binary(request.form.get('6')),binary(request.form.get('7')),binary(request.form.get('8')),),request.form['username'], request.form['password']), data=myresult)
     else:
	     return render_template('login.html')


@app.route('/form', methods=['POST', 'GET'])
def form():
@@ -128,5 +96,5 @@ def joke():
if __name__ == "__main__":
    #runs the application on the repl development server
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='192.168.1.40',port='8080')
    app.run(debug=True)
