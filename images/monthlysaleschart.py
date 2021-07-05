import numpy as np
import pylab
import matplotlib.pyplot as plt
import mysql.connector
import itertools
mydb =mysql.connector.connect(host='localhost',user='root',passwd='Alohomora123',db='FarmerPortal')
cursor = mydb.cursor()
cursor.execute("SELECT DATE from saletdy ")
date1=cursor.fetchall()
cursor.execute("SELECT total_sales from saletdy")
ts1=cursor.fetchall()
date=()
n_groups=12
for x in range(0,12):
	date=date+date1[x]
ts=()
for x in range(0,12):
	ts=ts+ts1[x]
fig,ax=plt.subplots()
index=np.arange(n_groups)
bar_width=0.5
opacity=0.6
rect1=ax.bar(date,ts,alpha=opacity,color='g',label="Monthly Sales")
ax.set_xlabel("Date")
ax.set_ylabel("Quantity")
ax.set_title("Monthly Sales")
ax.set_xticklabels(date,rotation = (45), fontsize = 5, va='bottom', ha='left')
ax.legend()
fig.tight_layout()
plt.savefig('monthlysales.jpg')