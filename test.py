import os 
import json 

f = open("test.json","r")
x = json.loads(f.read())
print(x,type(x))
print(x["key"])

f = open("test2.json","w")
f.write(json.dumps(x,indent=4))
