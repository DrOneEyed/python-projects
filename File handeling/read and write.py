a = open(r'D:\Vinu\codes\File handeling\let_her_go.txt','r+')
c = open(r'D:\Vinu\codes\File handeling\let.txt','w+')
#r - read
#w - write
#a - append
#r+ - read & write
#w+ - write & read
#a+ - write & read
bb = ' '
while bb:
    bb = str(a.readline())
    for j in bb:
        c.write(j)
    b = str(a.readline())
    print(b,end = ' ')
a.close()
c.close()
