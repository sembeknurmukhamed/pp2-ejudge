def fun(square):
   cnt = 1
   while cnt <= square:
      yield (cnt)**2
      cnt += 1

ctr = fun(int(input()))
for n in ctr:
   print(n)