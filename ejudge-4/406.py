def fib(x):
   a, b, cnt = 0, 1, 0
   while cnt < x:
      if cnt == x - 1:
         yield f"{a}"
         break
      yield f"{a},"
      a, b = b, a + b
      cnt += 1

num = fib(int(input()))
for i in num: print(i, end='')

