a = [1, 2, 4, 10, 12, 13, 49]
#binary sea
# 1 2 4 10 12 13 49
# 1 2 4  #12 13 49
f_ = False
f = 0
l = len(a)-1
b = int(input())#49
while f <= l and f_ == False:
    m = (f+l)//2
    if b == a[m]:
        f_ = True
    elif b>a[m]:
        f = m+1
    else:
        l = m-1
if f_:
    print('Found')
else:
    print('Not found')
