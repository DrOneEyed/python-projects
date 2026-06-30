s="aabbcc"
c=3
while True:
    if s[0] =='a':
        s=s[2:]
    elif s[-1]=='b':
        s=s[:2]
    else:
        c +=1
        break
print(s)
print(c)

