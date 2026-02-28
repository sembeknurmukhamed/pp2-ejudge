def square(x, y):
   num = x
   while num <= y:
      yield pow(num, 2)
      num += 1

a, b = map(int, input().split())
c = square(a, b)
for n in c:
   print(n)