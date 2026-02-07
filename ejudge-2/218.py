n = int(input())
first = {}

for i in range(1, n+1):
   s = input()
   if s not in first:
      first[s] = i

for s in sorted(first):
   print(s, first[s])