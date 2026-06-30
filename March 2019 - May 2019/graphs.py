#bar
from numpy import *
from matplotlib.pyplot import *
c = ['DEL', 'MUM', 'KOL', 'CHN']
p = [ 50, 40, 45, 49]
cc = [ 'red' , 'blue', 'black' , 'pink']
bar(c, p, width = 0.4, color = cc)
xlabel("Cities")
ylabel("Population")
title('gg') 
show()
#Dual Bar
A=[2,4,6,8]
b=[2.8,3.6,6.5,7.5]
x=arange(4)
bar(x,A,width=0.35,color='black',label = "len")
bar(x+0.35,b,width=0.35,color='blue',label = "width")
legend(loc="upper left")
show()
#Pie
cont = [17,6.8,12,75]
house = ['Forest', 'Air', 'Wild', 'Water']
pie(cont, labels = house, autopct = '%1.1f%%')
legend(loc="upper left")
savefig('graphssss.png')
show()
#Line
plot(p,x,color='cyan',label="cyan")
plot(p,b, color='blue',label="blue")
xlabel('X')
ylabel('Y')
title('GG')
legend(loc="upper left")
show()
#Horizontal Bar
c = ['DEL', 'MUM', 'KOL', 'CHN']
p = [ 50, 40, 45, 49]
cc = [ 'red' , 'blue', 'black' , 'pink']
barh(c, p, color = cc)
ylabel("Cities")
xlabel("Population")
show()

