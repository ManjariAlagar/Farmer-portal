from flask import Flask, request, render_template
from flask_mysqldb import MySQL
import MySQLdb
app=Flask(__name__)
@app.route("/")
def form():
    return render_template("signup.html")
@app.route("/",methods=["GET","POST"])
def side():
    if request.method == "POST":
        username=request.form["username"]
        password=request.form["password"]
        Phone_number=request.form["Phone_number"]
        email=request.form["email"]
        Account_type=request.form["Account_type"]
        Address1=request.form["Address1"]
        Address2=request.form["Address2"]
        City=request.form["City"]
        State=request.form["State"]
        db=MySQLdb.connect("localhost","root","Spassword","farmer_details")
        cur=db.cursor()
        cur.execute("INSERT INTO login(username,password,Phone_number,email,Account_type,Address1,Address2,City,State) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(username,password,Phone_number,email,Account_type,Address1,Address2,City,State))
        db.commit()
        return "cool" 
if __name__=="__main__":
    app.run(debug=True)