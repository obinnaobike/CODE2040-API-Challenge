import requests  
import json

data = {'token': "8c3ee7ee47e64108a7c2065ab225a89b",'github': "https://github.com/obinnaobike/CODE2040-API-Challenge"}
r = requests.post(url = "http://challenge.code2040.org/api/register", json = json.dumps(data))
print r

