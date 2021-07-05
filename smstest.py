
import requests

url = "https://www.smsgateway.center/SMSApi/rest/send"

querystring = {"userId":"mishri10","password":"Stupefy10","senderId":"SMSGAT","sendMethod":"simpleMsg","msgType":"text","mobile":"916384992711","msg":"This is my first message with SMSGateway.Center","duplicateCheck":"true","format":"json","scheduleTime":"2017-06-13 20:22:00"}

headers = {'cache-control': 'no-cache'}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)