#first repeated word in a string
a = "Ravi had been saying that he had been there"
b= ""
for i in a.split():
    print(i)
    if i in b:
        bb = i
        break
    else:
        b += i
        print("new str: ",b)
print("repeated word is: ",bb)
