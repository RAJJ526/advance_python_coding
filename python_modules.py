#import the moudle my_module and grreting
import platform
a=platform.system()
print(a)

import module
x=module.greeting("Raj")

import module
y=module.person1["country"]
print(y)

import platform
x=dir(platform)
print(x)

from module import person1
print(person1["age"])

#check present date and time
import datetime
x=datetime.datetime.now()
print(x)

#check year and day and month
import datetime
l=datetime.datetime.now()
print(l.year)
print(l.strftime("%A"))
print(l.strftime("%B"))

#program to create date and time
import datetime
h=datetime.datetime(2015,4,15)
print(h)


#mathmodule #maaaaaaaaaaaaaaaaaaaaaaaaattthhhhhhhhhhhhhhhhhhhhhmodddddddddddddddddduuuuuuuuullllllllllllle

#return square root of a number
import math
x=math.sqrt(64)
print(x)

#round a number upwards or downwards to nearest integer
import math
y=math.ceil(1.4)
z=math.floor(1.4)
print(y)
print(z)

#return the value of pi
x=math.pi
print(x)

#the abs function return the positive value of a number
# x=abs(-6.45)
# print(x)

#power of a number
# a=pow(3,3)
# print(a)

#python json module
#convert from json to python
import json
# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

import json
x='{"name":"jason", "age":30, "city":"Washington"}'
y=json.loads(x)
print(y["name"])

import json
#convert it to json string using json.dumps
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

import json
h=["string",45,6,7,8,8]
k=json.dumps(h)
print(k)












