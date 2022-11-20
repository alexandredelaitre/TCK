import requests
a=requests.get("https://api.streamelements.com/kappa/v2/store/5d7aa3881d4b677e436d2933/items").json()
print(a[1],"\n")
item=a[1]
thumbnail=item['thumbnail']
print(thumbnail)
description=item['description']
print(description)
userInput=item['userInput']
print(userInput)
cost=item['cost']
print(cost)
quantity=item['quantity']
print(quantity)
_id=item['_id']
print(_id)
name=item['name']
print(name)