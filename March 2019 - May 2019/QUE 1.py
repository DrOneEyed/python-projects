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


