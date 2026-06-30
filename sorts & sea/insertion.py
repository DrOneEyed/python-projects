a = '11 10 01 111 101'.split(' ')
#insertion sort
# 8 5 4 10 9
# 8 5 4 10 9
# 8 8 4 10 9
# 5 8 4 10 9
# 5 5 8 10 9
# 4 5 8 10 9
# 4 5 8 10 9
# 4 5 8 10 10
# 4 5 8 9 10
for i in range(len(a)):
    t = a[i]
    l = i
    for j in range(i-1,-1,-1):
        if a[j] > t:
            a[j+1] = a[j]
            l -= 1
        else:
            continue
    a[l] = t
print(a)
