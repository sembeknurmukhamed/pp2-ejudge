n = int(input())

g = 0
non = 0

for _ in range(n):
    parts = input().split()
    scope = parts[0]
    value = int(parts[1])

    if scope == "global":
        g += value
    elif scope == "nonlocal":
        non += value

print(g, non)