def fact(b):
    f=1
    for i in range(b,0,-1):
        f=f*i
    return f
a=int(input("Enter A Number To Find Its Factorial; "))
print("Factorial Of ",a," Is ",fact(a))
ff=1

def rec_fact(a,f):
    if a>0:
        return rec_fact(a-1,f*a)
    else:
        return f
print("Factorial Of ",a," Is ",rec_fact(a,ff))
