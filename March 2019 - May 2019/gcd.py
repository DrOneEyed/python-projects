def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
print(gcd(55,44))
a = int(input("Enter: "))
b=44

def rec_gcd(a,b):
    if b==0:
        return a
    else:
        return rec_gcd(b,a%b)
    
print(rec_gcd(a,b))
