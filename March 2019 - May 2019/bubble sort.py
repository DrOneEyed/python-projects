a=[54,20,78,336,115,10,20,0,2,3,44,5,66,44]
for ii in range(len(a)):
    for jj in range(len(a)-ii-1):
        if a[jj] > a[jj+1]:
            n=a[jj]
            a[jj]=a[jj+1]
            a[jj+1]=n
        else:
            continue
print(a)
a=[54,20,78,336,115,10,20,0,2,3,44,5,66,44]
i = len(a)-1

def rec(a,i):
    j = len(a)-i-1
    if a[j] > a[j+1] and i<len(a):
        n = a[j]
        a[j] = a[j+1]
        a[j+1] = n
        return rec(a,i-1)
    elif a[j] < a[j+1] and i<len(a):
        return rec(a,i-1)
    else:
        return a
print(rec(a,i))
