# Question 14
def read_line():
    a = open(r"D:\Vinu\codes\March 2019 - May 2019\file.txt", 'r')
    b = " "
    while b:
        b = str(a.readline())
        print(b, end = "")
    a.close()
    
# Question 15
def read_print_rem_punh():
    a = open(r"D:\Vinu\codes\March 2019 - May 2019\file.txt", 'r')
    b = ''';,.:'?!([{)]}_-/"'''
    c = open(r"D:\Vinu\codes\March 2019 - May 2019\filenews.txt",'w+')
    bb = " "
    while bb:
        bb = str(a.readline())
        for j in bb:
            if j not in b:
                c.write(j)
    a.close()
    c.close()
    
# Question 17
def read_write():
    a = open(r"D:\Vinu\codes\March 2019 - May 2019\file.txt", 'r')
    c = open(r"D:\Vinu\codes\March 2019 - May 2019\filenews.txt",'w+')
    b = " "
    while b:
        b = str(a.readline())
        c.write(b)
    a.close()
    c.close()

# Question 18
def to_the_count():
    a = open(r"D:\Vinu\codes\March 2019 - May 2019\Article.txt", 'r')
    b, d = 'to', 'the'
    s = 0
    cc = a.readlines()
    for i in cc:
        if b in i or d in i:
            s += 1
    print("Total Number Of 'to' And 'the' Present In Article.txt: ",s)
    a.close()

# Question 19
def cap_count():
    a = open(r"D:\Vinu\codes\March 2019 - May 2019\Poem.txt", 'r')
    s = 0
    bb = " "
    while bb:
        bb = str(a.readline())
        for j in bb:
            if j.isupper():
                s += 1
    print("Total Number Of Capital Letters Present In Poem.txt: ",s)
    a.close()

# Question 20
def a_new():
    a = open(r"D:\Vinu\codes\March 2019 - May 2019\file.txt", 'r')
    c = open(r"D:\Vinu\codes\March 2019 - May 2019\filenew1.txt", 'w+')
    b = "a"
    bb = " "
    while bb:
        bb = str(a.readline())
        if b in bb:
            c.write(bb)
    a.close()
    c.close()
