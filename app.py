# importing the modules
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors

# app config
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = 'Y8RYDnrC11'
app.config['MYSQL_PASSWORD'] = 'vbNTSPoO7o'
app.config['MYSQL_DB'] = 'Y8RYDnrC11'
mysql = MySQL(app)
app.secret_key = 'returnzero'


# routes
@app.route("/register",methods=["GET","POST"])
def register_account():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO User(username,email,password,role) VALUES(%s,%s,%s,%s)",(username,email,password,0))
        mysql.connection.commit()
        return "Account Successfully Created"
    return render_template("register.html")

# run server
if __name__ == "__main__":
    app.run(debug=True)


"""
Username: Y8RYDnrC11
Database name: Y8RYDnrC11
Password: vbNTSPoO7o
Server: remotemysql.com
Port: 3306
"""