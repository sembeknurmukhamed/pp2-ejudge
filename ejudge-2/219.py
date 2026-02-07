n = int(input())
watched = {}

for i in range(n):
   s, k = input().split()
   k = int(k)
   watched[s] = watched.get(s, 0) + k

for name in sorted(watched):
   print(name, watched[name])
