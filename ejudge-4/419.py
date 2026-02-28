import math

def segment_to_origin_dist(ax, ay, bx, by):
    dx, dy = bx - ax, by - ay
    len_sq = dx*dx + dy*dy
    if len_sq == 0:
        return math.hypot(ax, ay)
    t = ((-ax) * dx + (-ay) * dy) / len_sq
    t = max(0.0, min(1.0, t))
    px, py = ax + t * dx, ay + t * dy
    return math.hypot(px, py)

r  = float(input())
ax, ay = map(float, input().split())
bx, by = map(float, input().split())

if segment_to_origin_dist(ax, ay, bx, by) >= r - 1e-9:
    print(f"{math.hypot(bx-ax, by-ay):.10f}")

else:
    dA = math.hypot(ax, ay)
    dB = math.hypot(bx, by)

    alphaA = math.atan2(ay, ax)
    alphaB = math.atan2(by, bx)

    deltaA = math.acos(r / dA)
    deltaB = math.acos(r / dB)

    tan_A = math.sqrt(dA*dA - r*r) 
    tan_B = math.sqrt(dB*dB - r*r)

    best = float('inf')

    for sA in (+1, -1):
        for sB in (+1, -1):
            angle1 = alphaA + sA * deltaA
            angle2 = alphaB + sB * deltaB

            diff = abs(angle1 - angle2) % (2 * math.pi)
            if diff > math.pi:
                diff = 2 * math.pi - diff
            arc = r * diff

            best = min(best, tan_A + arc + tan_B)

    print(f"{best:.10f}")