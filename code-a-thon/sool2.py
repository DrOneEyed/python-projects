string = list(map(str, input().split(" ")))
the = 0
a = 0
for i in range(len(string)):
    string[i].replace("\"", "")
    if string[i] == "a"  and string[i+1][0] not in "aeiou" or string[i] == "A":
        a+=1
    elif string[i] == "the" and string[i+1][0] in "aeiou":
        the+=1
print("A " + str(a))
print("The " + str(the))