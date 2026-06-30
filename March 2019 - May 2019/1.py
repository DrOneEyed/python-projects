from tkinter import *
w=Tk()
w.geometry('500x500+150+300')
w.title("HELLO")
p=PhotoImage(file='(1).png')
b= Button(text = "YO",width=2,height=3,bg='blue',fg='red',activebackground='purple',activeforeground='black',
          bd=10,cursor="heart",underline=2,image=p,highlightthickness=200).pack()
#Button(text = "YO",relief=RAISED, cursor="circle" ).pack() #heart,plus,clock,dotbox,man,mouse,pirate,sizing.star,hand2,pencil,question_arrow,boat
#Button(bitmap = "error").pack() #hourglass,info,gray75,gray50,gray25,gray12,questhead,warning,question
#Button(text = 'some').place(x=150,y=150) & .pack(pady=220) & .grid(row=1, column=0)
#Button(text = 'some', relief = RAISED).pack() #SUNKEN,FLAT,GROOVE,RIDGE
#Button(text = 'some', state=DISABLED).pack()
#l= Label(text = "YOOOO", fg='white', bg = 'black').grid(row=1, column=0)
w.mainloop()
cursor = 'pencil'
#file
a=open(r"D:\Vinu\codes\file.txt")
b='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
c=open(r"D:\Vinu\codes\filenew.txt",'w')
for i in a:
    for j in a.readline():
        if j not in b:
            c.write(i)
        else:
            continue
a.close()

c.close()

#binary search
a=[0, 2, 3, 5, 10, 20, 20, 44, 44, 54, 66, 78, 115, 336]
b=int(input("Enter A Element: "))
fo=False
f=0
l=len(a)-1
#with out rec
while f<=l and fo==False:
    m=(f+l)//2
    if b==a[m]:
        fo=True
    elif b>a[m]:
        f=m+1
    else:
        l=m-1
if fo==True:
    print("Number At ",m+1," Position.")
else:
    print("Number is not present in the list.")
#with rec
def rec_binsec(a,b,f,l):
    m=(f+l)//2
    if b==a[m]:
        return m
    elif b>a[m] and f<l:
        f=m+1
        return rec_binsec(a,b,f,l)
    elif b<a[m] and f<l:
        l=m-1
        return rec_binsec(a,b,f,l)
    else:
        return "Number is not present in the list."    
print(rec_binsec(a,b,f,l))

#bubble sort
a=[54,20,78,336,115,10,20,0,2,3,44,5,66,44]
'''for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            n=a[j]
            a[j]=a[j+1]
            a[j+1]=n
        else:
            continue'''
print(a)
b=0

def rec_(a,b):
    if a[b]> a[b+1]:
        n=a[b]
        a[b]=a[b+1]
        a[b+1]=n
        return rec_(a,b+1)
    elif a[len(a)-2]<a[len(a)-1]:
        return a
print(rec_(a,b))


#insertion sprt
a=[54,20,78,336,115,10,20,0,2,3,44,5,66,44]
for i in range(len(a)):
    temp=a[i]
    l=i
    for j in range(i-1,-1,-1):
        if a[j]>temp:
            a[j+1]=a[j]
            l=l-1
        a[l]=temp
print(a)


#modules
import time
print(time.__name__)
from math import sqrt,pow,pi
print(sqrt(4))
print(pow(2,2))
print(pi)
#x=int(input("Enter A Number: "))
x=35
print(hex(x))
print(oct(x))
#c=float(input("Enter A Decimal Number: "))
c=678.0912345678
print(int(c))
print(round(c,4))
import random as ra
print(ra.random())
import math
print(math.ceil(ra.random()))

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
d=int(input("Enter A URL: "))
aa=url.request.urlopen(d)
bb=aa.geturl()
print("Now Openning The The Website.... ")
