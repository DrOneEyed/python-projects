a = [1, 2, 4, 10, 12, 13, 49]
#linear search
#1,2,4,10,12
b = int(input())#12
f = False
for i in a:
    if b == i:
        f = True
        print('Found')
        break
    elif f != True and i == len(a)-1:
        print('Not Found')
