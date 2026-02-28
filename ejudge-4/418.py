x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

t = y1 / (y1 + y2)
rx = x1 + t * (x2 - x1)

print(f"{rx:.10f} {0:.10f}")