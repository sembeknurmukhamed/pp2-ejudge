n, numbers = int(input()), list(map(int, input().split()))
for i in range(n): numbers[i] **= 2
print(*numbers)

