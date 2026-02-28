def numbers(x):
   num = x
   while num >= 0:
      yield num
      num -= 1

n = numbers(int(input()))
for i in n:
   print(i)