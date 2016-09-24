import requests  
import json

data = {'token':'8c3ee7ee47e64108a7c2065ab225a89b'}
r = requests.post("http://challenge.code2040.org/api/haystack", data)
print r.json()
jsonData = str(r.text)
d = json.loads(jsonData)
for i in xrange(len(d["haystack"])):
    if d["needle"] == d["haystack"][i]:
        result = i
data2 = {'token':'8c3ee7ee47e64108a7c2065ab225a89b', 'needle': result}
r2 = requests.post("http://challenge.code2040.org/api/haystack/validate", data2)

print r2.status_code
print r2.text
