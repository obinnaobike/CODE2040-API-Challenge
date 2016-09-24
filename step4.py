import requests  
import json

data = {'token': '8c3ee7ee47e64108a7c2065ab225a89b'}
r = requests.post("http://challenge.code2040.org/api/prefix", data)
print r.json()
#print r.json()["prefix"]
#print r.json()["array"]
print r.status_code
pre = r.json()["prefix"]
arr = r.json()["array"]
def prefix(prefix, array):
    newarray = []
    for i in xrange(len(array)):
        if array[i][0:len(pre)] != pre:
            newarray.append(array[i])
    """for i in xrange(len(r.json()["array"])):
        if r.json()["array"][i][0:4] != r.json()["prefix"]:
            newarray.append(str(r.json()["array"][i]))"""
    return newarray

result = prefix(pre,arr)
arr = [0]
print result
data1 = {'token': '8c3ee7ee47e64108a7c2065ab225a89b','array': result}
url = "http://challenge.code2040.org/api/prefix/validate"
r1 = requests.post(url, json=data1)
print r1

