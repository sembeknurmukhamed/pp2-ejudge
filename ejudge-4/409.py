def pow_of_two(x):
   num = 0
   while num <= x:
      yield pow(2, num)
      num += 1

n = pow_of_two(int(input()))
for i in n: print(i, end=" ")