from flask import Flask, request, render_template
from flask_mysqldb import MySQL
import MySQLdb
app=Flask(__name__)
@app.route("/")
def form():
    return render_template("login.html")
@app.route("/",methods=["GET","POST"])
def side():
    if request.method == "POST":
        username=request.form["username"]
        password=request.form["password"]
        Account_type=request.form["Account_type"]
        db=MySQLdb.connect("localhost","root","Spassword","farmer_details")
        cur=db.cursor()
        cur.execute("select *from farmer_details.login where username='"+ username + "' and password='" + password +"'")
        db=cur.fetchone()
        if db is None:
            return "username and password is invalid"
        else:
            return "cool"
if __name__=="__main__":
    app.run(debug=True)