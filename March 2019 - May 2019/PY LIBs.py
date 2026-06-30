import time
print(time.__name__)
from math import sqrt,pow,pi
print(sqrt(4))
print(pow(2,3))
print(pi)
#x=int(input("Enter A Number: "))
x=35
print(hex(x))
print(oct(x))
#c=float(input("Enter A Decimal Number: "))
c=678.0912345678
print(round(c,4))
import random as ra
print(ra.random())
print(ra.randint(2,5))



#URL
import urllib as url
import webbrowser as web
import requests
g=input("Enter A URL: ")
w= url.request.urlopen(g)
html=w.read()
data=w.getcode()
u=w.geturl()
h=w.headers
inf=w.info()
print("The URL is",u)
print("HTTP Status Code is: ",data)
print("Headers \n",h)
print("INFO \n",inf)
print("Now Opening The URL")
web.open_new(u)

