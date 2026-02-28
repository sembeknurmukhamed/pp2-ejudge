def repeat(nums, x):
   for i in range(x):
      for j in nums:
         yield j
   
res = repeat(list(input().split()), int(input()))
for i in res:
   print(i, end=" ")
       
      

