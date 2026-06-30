a = [10,12,4,2,13,49,1]
#selection sort
#1 12 4 2 13 49 10
#1 2 4 12 13 49 10
#1 2 4 12 13 49 10
#1 2 4 10 13 49 12
#1 2 4 10 12 49 13
#1 2 4 10 12 13 49
for i in range(len(a)):#0
    for j in range(i+1, len(a)):#1
        if a[i]>a[j]:
            k = a[i]
            a[i] = a[j]
            a[j] = k
            #a[i], a[j] = a[j], a[i]
        else:
            continue
print(a)
