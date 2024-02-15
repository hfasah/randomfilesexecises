'''
Reading a  jason file and pulling  specific values from the json file.
'''

import json
f = open("/Users/hippolyteasah/Library/CloudStorage/OneDrive-Personal/Python/Python Training/users.json","r")
data = f.read()
print(type(data))
data1 = json.loads(data)
print(type(data1))
print(data1[0]["name"],data1[0]["address"]["city"],data1[0]["address"]["geo"] )



''' 
first Crete a folder

# import json
# import requests

# output = requests.get('https://jsonplaceholder.typicode.com/users')
# print(output.json()[0])

# print(output)

'''



