a = [10,12,4,2,13,49,1]
#bubble sort
# 5 1 4 2 8
# 1 5 4 2 8
# 1 4 5 2 8
# 1 4 2 5 8
# 1 4 2 5 8
# 1 2 4 5 8

for i in range(len(a)):#0   #7
    for j in range(len(a)-i-1):#7-0-1=6
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
        else:
            continue
print(a)
