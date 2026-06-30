def to_string(n,b):
   conver_tString = "0123456789ABCDEF"
   if n < b:
       print("C:: ",n)
       print(conver_tString[n])
       print("#########################################")
       return conver_tString[n]
   else:
       print("A:: ",n," : ",b)
       a=to_string(n//b,b)
       c=conver_tString[n % b]
       print("B:: ",a," : ",c," : ",a+c)
       print("#########################################")
       return to_string(n//b,b) + conver_tString[n % b]

print(to_string(2835,16))
