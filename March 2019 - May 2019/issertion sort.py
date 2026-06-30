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
s=0
for i in range(1,10):
    s+=i
print(s)
