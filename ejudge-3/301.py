def valid_number(x):
   valid = False
   
   for i in str(x): 
      if int(i) % 2 != 0: break
   else: valid = True
   
   return valid

num = int(input())

if valid_number(num): print("Valid")
else: print("Not valid")

