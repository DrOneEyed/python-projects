ff = open(r'names.txt','r')
n = str(input())
f = False
for i in ff.read().split(','):
    if n == i:
        f = True
        print('Found')
        break
    else:
        continue
if f == False:
    print('Not Found')
ff.close()
