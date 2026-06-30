from math import *
from matplotlib.pyplot import *
from numpy import *
sinnn = 0
s=[]
def func_e(x, n,sinnn,s):
    for i in range(n+1):
        a = (-1)**n
        b = radians(x)
        c = (2*n)+1
        d = b**c
        e = factorial(c)
        sinnn += a*d/e
        s.append(sinnn)
        print(i,"th value of sin(",int(x),") is: ",float(sinnn))
n = int(input("Enter Value Of N: "))
x = float(input("Enter Value For X In Degre: "))
func_e(x,n,sinnn,s)

x = linspace(0,n)
y = linspace(s[0],s[-1])
plot(x, y, color='cyan', linewidth = 3, marker='o', markerfacecolor='black', markersize=8)
xlabel("X axis")
ylabel("Y axis")
title("Graph")
show()
