import requests  
import json
import dateutil.parser
import datetime
import iso8601

data = {'token':'8c3ee7ee47e64108a7c2065ab225a89b'}
r = requests.post('http://challenge.code2040.org/api/dating', data)
print r.json()
jsonData = r.json()
date = jsonData['datestamp']
inter = jsonData['interval']


def datestamp(interval, thedate):
	
	interval = int(interval)

	date = iso8601.parse_date(thedate)
	interval = datetime.timedelta(0, interval)
	
	final = date + interval

	final = final.isoformat()
	
	format1 = final.split('+')[0]
	format1 += 'Z'
	return format1

result = datestamp(inter, date)
print result
data3 = {'token': '8c3ee7ee47e64108a7c2065ab225a89b', 'datestamp': result}
r3 = requests.post('http://challenge.code2040.org/api/dating/validate', data3)
print r3.status_code

