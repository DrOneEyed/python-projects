'''Write a program that asks the user the dat number in a year in the range (2-365)
and asks the first day of the year(Sun. Mon etc.). Then the program should display
the day on the day-number that has been input.'''
x = int(input('Enter the number of day: '))
d = input('Enter the first day of year: ')
l = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print(l[l.index(d) + x%7 - 1]) 

'''Write a program that reads a date as an integer in the format DDMMYYYY. The program
will call a function that prints print out the date in the format <Month-Name><space><day>,<year>'''
i = int(input("Enter a date in format(DDMMYYYY): "))
n = str(i)
m = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', "Aug", "Sep", "Oct", 'Nov', 'Dec']
print(m[int(n[2:4])-1], n[0:2],',',n[-4:])

#PG 32, que17
for i in range(1, 10):
    for j in range(i, (i*9)+1, i):
            print(j, end="\t")
    print('\n')

#GG
s = str(input("Enter A string: "))
ss = s.replace("enter", "")
print(ss)
a = 0
sc = 0
t = 0
for i in ss:
    if i.isalpha():
        a += 1
        t += 1
    elif i.isdigit():
        t += 1
        continue
    else:
        sc += 1
        t += 1
print("No. of Alpha =",a,"\nAnd % is",(a/t)*100)
print("No. of Spec Ch =",sc,"\nAnd % is",(sc/t)*100)

#GGG
a = [1,2,3,4]
b = [1,2,3,4,5]
def add_l(a,b):
    nl = []
    for i in range(0, len(a)):
        if i<len(b):
            nl.append(a[i] + b[i])
        else:
            nl.append(a[i])
    for j in range(0,len(b)):
        nl.append(b[j])
    print(nl)
if len(b)>len(a):
    add_l(b,a)
else:
    add_l(a,b)

'''Write a Python program that takes a string and encode it
that the amount of symbols would be represented by integer and the symbol.'''
s = str(input("Enter A Line: "))
n = ""
c = 0
lc = s[0]
for i in range(0, len(s)):
    if lc == s[i]:
        c += 1
    else:
        n += str(c) + lc
        c = 0
        lc = s[i]
        c += 1
n += str(c) + lc
print(n)


