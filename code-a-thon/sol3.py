#import numpy as np
import time
def polygonArea(X, Y, n):
    area = 0
    j = n - 1
    for i in range(0,n):
        area += (X[j] + X[i]) * (Y[j] - Y[i])
        j = i # j is previous vertex to i
    return int(abs(area / 2.0))
strat_time = time.time()
a = open(r'C:\Codes\Python\Py\code-a-thon\input.txt','r+')
b = list(map(str, a.readline().split(" ")))
area = 0
'''def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))'''

xl = []
yl = []
for i in b:
    x, y = map(int, i.split(","))
    xl.append(x)
    yl.append(yl)
polygonArea(xl,yl,len(xl))
print(time.time() - strat_time)