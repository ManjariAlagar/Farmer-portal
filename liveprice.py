import requests
from flask import *
from bs4 import BeautifulSoup as bs
import json
app = Flask(__name__)
@app.route('/')
def itemGet():
	link1 = "https://rates.goldenchennai.com/vegetable-price/madurai-vegetable-price-today/"
	r = requests.get(link1)
	if ( r.status_code != 200 ):
		print("Link failed ",link1)
	page = r.text
	soup = bs(page,'html.parser')
	veg_details = soup.find_all('td')
	vegDetailsDict = []
	for items in veg_details:
		vegDetailsDict.append(items.text)
	link2 = "https://rates.goldenchennai.com/fruit-price/madurai-fruit-price-today/"
	r = requests.get(link2)
	if ( r.status_code != 200 ):
		print("Link failed ",link2)
	page = r.text
	soup = bs(page,'html.parser')
	fruit_details = soup.find_all('td')
	fruitDetailsDict = []
	for items in fruit_details:
		fruitDetailsDict.append(items.text)
	return render_template('index.html',price=vegDetailsDict,fruits=fruitDetailsDict)

if __name__=="__main__":
	app.run()
