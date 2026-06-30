a=str(input("Enter A Number To Find The Sum Of Its Digits: "))
s=0
for i in range(len(a)):
    s=s+ int(a[i])**2
print("Sum Of ",a," = ",s)
x=a
y=0
z=len(x)-1
def rec_(x,y,z):
    if z>=0:
        y=y+ (int(x[z])**2)
        return rec_(x,y,z-1)
    else:
        return y
print("Sum Of Digits Of ",x," = ",rec_(x,y,z))
