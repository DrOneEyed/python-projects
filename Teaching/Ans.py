def difference(n):
    if n <= 12:
        return 12 - n
    else:
        return (n - 12) * 2 

def isPresentList(group_data, n):
   for value in group_data:
       if n == value:
           return True
   return False

def listCount(nums, nc):
  count = 0  
  for num in nums:
    if num == nc:
      count = count + 1

  return count

def add_numbers(a, b):
   if not (isinstance(a, int) and isinstance(b, int)):
       return "Inputs must be integers!"
   return a + b

def distPoint():
    import math
    p1 = [4, 0]
    p2 = [6, 6]
    distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

difference(12)

def setDifference():
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    print(color_list_1.difference(color_list_2))
    print(color_list_2.difference(color_list_1))