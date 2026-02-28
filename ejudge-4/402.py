def fun(even):
   cnt = 0
   while cnt <= even:
      if cnt == even or cnt == even - 1:
         yield f"{cnt}"
         break
      yield f"{cnt},"
      cnt += 2

ctr = fun(int(input()))
for n in ctr:
   print(n, end='')