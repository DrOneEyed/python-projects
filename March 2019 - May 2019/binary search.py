a=[0, 2, 3, 5, 10, 20, 20, 44, 44, 54, 66, 78, 115, 336]

fo=False
f=0
l=len(a)-1
print(a)
b=int(input("Enter A Element: "))

#with out rec
while f<=l and fo==False:
    m=(f+l)//2
    if b==a[m]:
        fo=True
    elif b>a[m]:
        f=m+1
    else:
        l=m-1
if fo==True:
    print("Number At ",m+1," Position.")
else:
    print("Number is not present in the list.")
#with rec
def rec_binsec(a,b,f,l):
    m=(f+l)//2
    if b==a[m]:
        return m+1
    elif b>a[m] and f<l:
        f=m+1
        return rec_binsec(a,b,f,l)
    elif b<a[m] and f<l:
        l=m-1
        return rec_binsec(a,b,f,l)
    else:
        return "Number is not present in the list."    
print(rec_binsec(a,b,f,l))


