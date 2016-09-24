import requests  
import json

data = {'token':'8c3ee7ee47e64108a7c2065ab225a89b'}
dat = json.dumps(data)
r = requests.post("http://challenge.code2040.org/api/reverse", data)
# jsonData = json.loads(r.json())
print dat
print r.text
print r.status_code 

def reverse(string):
	output = ''
	for i in range(len(string)-1,-1,-1):
		output = output + string[i]
	return output
    
result = reverse(r.text)
print result
data2 = {'token': '8c3ee7ee47e64108a7c2065ab225a89b', 'string': result}
r2= requests.post('http://challenge.code2040.org/api/reverse/validate', data2)
print r2.text
print r2.status_code 

