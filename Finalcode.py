import mysql.connector
from flask import *
import requests
import mysql.connector
from bs4 import BeautifulSoup as b 
import json
app=Flask(__name__)
@app.route("/",methods=['POST','GET'])
def login():
	if request.method == "POST":
		count=0
		username=request.form["username"]
		password=request.form["password"]
		option=request.form["options"]
		db =mysql.connector.connect(host='localhost',user='root',passwd='Alohomora123',db='FarmerPortal')
		cur=db.cursor()
		cur.execute("select * from users ")
		data=cur.fetchall()
		print(data)
		for i in data:
			print(i[0]+" "+i[1]+" "+i[4])
			if i[0]==username and i[1]==password and i[4]==option:
				count+=1
				if option=="Buyer" or option=="Customer":
					return render_template("about.html")
				else:
					return render_template("about1.html")
		if count==0:
			return "Wrong credentials"
	if "signup" in request.form:
		return render_template("signup.html")
	elif "upload" in request.form:
		return render_template("shop.html")
	elif "shop" in request.form:
		return render_template("shopb.html")
	else:
		return render_template("login.html")
@app.route("/signup",methods=["GET","POST"])
def signup():
	if request.method == "POST":
		username=request.form["username"]
		password=request.form["password"]
		Phone_number=request.form["Phone_number"]
		email=request.form["email"]
		option=request.form["options"]
		Address1=request.form["Address1"]
		Address2=request.form["Address2"]
		City=request.form["City"]
		State=request.form["State"]
		db =mysql.connector.connect(host='localhost',user='root',passwd='Alohomora123',db='FarmerPortal')
		cur=db.cursor()
		cur.execute("INSERT INTO users(username,password,phno,email,account_type,address1,address2,city,state) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(username,password,Phone_number,email,Account_type,Address1,Address2,City,State))
		db.commit()
		db.close()
	if "signingup" in request.form:
		return render_template("login.html")
	else:
		return render_template("signup.html")
@app.route("/uploadstock",methods=["GET","POST"])
def uploadstock():
	if request.method == "POST":
		farmer_id=request.form["farmer_id"]
		product_name=request.form["product_name"]
		product_id=request.form["product_id"]
		product_detail=request.form["product_detail"]
		Market_price=request.form["market_price"]
		final_price=request.form["final_price"]
		product_image=request.form["product_image"]
		db =mysql.connector.connect(host='localhost',user='root',passwd='Alohomora123',db='FarmerPortal')
		cur=db.cursor()
		cur.execute("INSERT INTO stock(fid,product_name,pid,product_detail,Market_price,final_price,product_image) VALUES(%s,%s,%s,%s,%s,%s,%s)",(farmer_id,product_name,product_id,product_detail,Market_price,final_price,product_image))
		db.commit()
		db.close()
		return render_template("Success.html")
	return render_template('shop.html')
@app.route("/inventorydisplay",methods=["GET" ,"POST"])
def inventorydisplay():
	db =mysql.connector.connect(host='localhost',user='root',passwd='Alohomora123',db='FarmerPortal')
	cur=db.cursor()
	query="select*from stock "
	cur.execute(query)
	return render_template("shopB.html", m=cur.fetchall())
@app.route("/ratedisplay",methods=["POST","GET"])
def ratedisplay():
	url=["https://rates.goldenchennai.com/vegetable-price/madurai-vegetable-price-today/"]
	r=request.get(link)
	if(r.status_code!=200):
		print("Link failed")
		continue
	page=r.text
	soup=bs(page,"html.parser")
	rates=soup.find_all('td')
	ratesDict={}
	for rate in rates:
		
@app.route("/wishlist",methods=['GET','POST'])
def wishlist():
	return render_template("wishlist.html")
@app.route("/products",methods=['GET','POST'])
def products():
	return render_template("product-single.html")
@app.route("/cart",methods=['GET','POST'])
def cart():
	return render_template("cart.html")
@app.route("/contact",methods=['GET','POST'])
def contact():
	return render_template("contact.html")
@app.route("/checkout",methods=['GET','POST'])
@app.route("/checkout",methods=['GET','POST'])
def checkout():
	return render_template("checkout.html")
@app.route("/home",methods=['GET','POST'])
def home():
	return render_template("about.html")
@app.route("/home1",methods=['GET','POST'])
def home1():
	return render_template("about1.html")
@app.route("/payment",methods=['GET','POST'])
def payment():
	return render_template("payment.html")
@app.route("/result",methods=["POST","GET"])
def result():
	if request.method == 'POST':
		search=request.form["product_name"]
		db =mysql.connector.connect(host='localhost',user='root',passwd='Alohomora123',db='FarmerPortal')
		cur=db.cursor()
		query="select * from stock where product_name="+search
		cur.execute(query)
		m=cur.fetchall()
		cur.close()
	return render_template("searchresult.html" ,m=m)	
@app.route("/sendsms",methods=['GET','POST'])	
def sendsms():
	pidr="ASDEFG23"
	username="Mishri"
	addr="11,North Kambar St;S.S.Colony"
	upnho="9486503327"
	mydb =mysql.connector.connect(host='localhost',user='root',passwd='Alohomora123',db='FarmerPortal')
	cursor = mydb.cursor()
	cursor.execute("SELECT phno from saletdy where 'pid'=pidr ")
	phno=("989499937")
	url = "https://www.fast2sms.com/dev/bulk"
	payload = "sender_id=FSTSMS&message=You have an order from+username+for+pidr&language=English&route=p&numbers=9894999327,9486503327"
	headers = {
 'authorization': "Cg8j2WO9Je4H0ZQ3fvnLU1io5MpduSsFwPqNcraAR6xbzKBGyTbJcZaIYKF7i5xnXuyUDdMHtfpk6q9g",
 'Content-Type': "application/x-www-form-urlencoded",
 'Cache-Control': "no-cache",
	}
	response = requests.request("POST", url, data=payload, headers=headers)
	print(response.text)

if __name__=="__main__":
    app.run(debug=True)
	