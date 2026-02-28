import math

r = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx, dy = x2-x1, y2-y1
a = dx*dx + dy*dy
b = 2*(x1*dx + y1*dy)
c = x1*x1 + y1*y1 - r*r

if a == 0:
    print(f"{0:.10f}")
else:
    disc = b*b - 4*a*c
    if disc < 0:
        print(f"{0:.10f}")
    else:
        s = math.sqrt(max(0, disc))
        t1 = max(0.0, min(1.0, (-b-s)/(2*a)))
        t2 = max(0.0, min(1.0, (-b+s)/(2*a)))
        print(f"{(t2-t1)*math.sqrt(a):.10f}")