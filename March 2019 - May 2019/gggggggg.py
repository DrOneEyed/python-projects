#Que 1
def cube_n(a = 2 ):
    print("Cube Of ", a ,' Is ', a**3)

def call_1():
    a = str(input("Enter a Number: "))
    if a == "":  
        cube_n()
    else:
        b = int(a)
        cube_n(b)
# QUE 2
def call_2():
    a = int(input("Enter First Number: "))
    b = int(input("Enter Last Number: "))
    l = []
    c = (b-a)/5
    print("The Difference Between Numbers Should Be ",c)    
    for i in range(5):
        l.append(a)
        a += c
    print("5 Equidistant Numbers Between ",a," And ",b,"Are: ")
    dd = 0
    for i in l:
        dd += 1
        print(dd,") ",i)
    
#Que 3
def char_len(a,b):
    if a == b:
        print("They Are Equal !! ")
    else:
        print("They Are Not Equal !!")
def call_3():
    a =  str(input("Enter 1st String: "))
    b = str(input("Enter 2nd String: "))
    if len(a)>1 or len(b)>1:
        print("Enter Only One Letter !!")
        call_3()
    else:
        char_len(a,b)

#Que 4
def re(a):
    b  = 0
    for i in a:
        b +=1
        print(b,")", i) 
def call_4():
    a = open(r"C:\Users\ICT-S2\Desktop\python stuff misc\ggggggggggggg.txt",'r')
    re(a)
                      
