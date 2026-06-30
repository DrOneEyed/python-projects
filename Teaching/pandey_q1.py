from itertools import combinations
def FindMultipleOf3InGroup(arr):
    mul3 = 0
    list_combinations = list()
    sample_set = set(arr)
    for n in range(len(sample_set) + 1):
        list_combinations += list(combinations(sample_set, n))
    
    for i in list_combinations:
        if len(i) == 3 or len(i) == 2:
            sum = 0
            for j in i:
                sum += j
            if sum%3 == 0:
                print(i)
                mul3 += 1
    return mul3

arr = [4,5,3,6,2]
print(FindMultipleOf3InGroup(arr))