from flask import Flask, request, render_template
from flask_mysqldb import MySQL
import MySQLdb
app=Flask(__name__)
@app.route("/")
def form():
    return render_template("shop.html")
@app.route("/",methods=["GET","POST"])
def side():
    if request.method == "POST":
        farmer_id=request.form["farmer_id"]
        product_name=request.form["product_name"]
        product_id=request.form["product_id"]
        product_detail=request.form["product_detail"]
        Market_price=request.form["Market_price"]
        final_price=request.form["final_price"]
        product_image=request.form["product_image"]
        db=MySQLdb.connect("localhost","root","Spassword","farmer_details")
        cur=db.cursor()
        cur.execute("INSERT INTO stock(farmer_id,product_name,product_id,product_detail,Market_price,final_price,product_image) VALUES(%s,%s,%s,%s,%s,%s,%s)",(farmer_id,product_name,product_id,product_detail,Market_price,final_price,product_image))
        db.commit()
        return "cool" 
if __name__=="__main__":
    app.run(debug=True)