def fun(x):
   num = 0
   while num <= x:
      if num%3 == 0 and num%4 == 0:
         yield num
      num += 1

ctr = fun(int(input()))
for n in ctr:
   print(n, end=' ')