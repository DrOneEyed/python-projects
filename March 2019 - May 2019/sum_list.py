a = [1,4,6,3]
b = len(a)-1
s = 0
def sum_list(a,b,s):
    if b>=0:
        s += a[b]
        b -= 1
        return sum_list(a,b,s)
    else:
        return s
print("Sum Of Numbers Of List: ",sum_list(a,b,s))
