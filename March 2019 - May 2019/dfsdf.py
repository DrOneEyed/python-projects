a = open(r"D:\Vinu\codes\March 2019 - May 2019\file.txt", 'r')
stra = " "
while stra:
    stra = str(a.readline())
    print(stra, end = "")
a.close()
