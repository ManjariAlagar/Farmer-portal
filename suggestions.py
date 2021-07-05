from flask import *
import datetime
import mysql.connector
app=Flask(__name__)
filename=" "
def showsuggestions(filename):
	mydb =mysql.connector.connect(host='localhost',user='root',passwd='Alohomora123',db='FarmerPortal')
	cursor = mydb.cursor()
	filename=filename+".html"
	query="SELECT * FROM  productreviews WHERE  'pname'=%s"
	cursor.execute(query,(filename,))
	print(query)
	return render_template(filename)
@app.route('/',methods=['GET','POST'])
def suggestions():
	if request.method=='POST':
		username=request.form.get('username')
		reviewtext=request.form.get('review')
		pid=request.form.get('pid')
		now = datetime.datetime.now()
		rating=request.form.get('rating')
		pname=request.form.get('pname')
		mydb =mysql.connector.connect(host='localhost',user='root',passwd='Alohomora123',db='FarmerPortal')
		cursor = mydb.cursor()
		query="INSERT INTO productreviews(pid,review,rating,dateuploaded,username) VALUES(%s,%s,%s,%s,%s)"
		cursor.execute(query,(pid,reviewtext,rating,now,username))
#close the connection to the database.
		mydb.commit()
		cursor.close()
		showsuggestions(pname)
	return render_template("suggestions.html")
if __name__=='__main__':
	app.run(debug=True)
