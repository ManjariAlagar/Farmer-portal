from flask import Flask, request, render_template
import mysql.connector
app=Flask(__name__)
@app.route("/",methods=["GET" ,"POST"])
def result():
    db=mysql.connector.connect("localhost","root","Spassword","farmer_details")
    cur=db.cursor()
    query="select*from stock "
    cur.execute(query)
    return render_template("shopB.html", m=cur.fetchone())   
if __name__=="__main__":
    app.run(debug=True, port=3360)