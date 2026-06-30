a = [1, 2, 3, 5, 10, 20, 20, 44, 44, 54, 66, 78, 115, 336]
b = int(input("Enter A Number To Search: "))
f = False
fi = 0
L = len(a) - 1
while f == False:
    m = (fi + L)//2
    if b == a[m]:
        f = True
    elif b > a[m]:
        fi = m + 1
    elif b < a[m]:
        L = m - 1
    else:
        break
if f == True:
    print("Number Found At ",m+1)

else:
    print("Number Is Nott Present In The list. ")
