n, numbers = int(input()), list(map(int, input().split()))
for i in range(len(numbers)):
   if numbers[i] not in numbers[0: i]:
      print("YES")
   else: print("NO")
