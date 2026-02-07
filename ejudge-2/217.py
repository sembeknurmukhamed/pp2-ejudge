n = int(input())
freq = {}

for i in range(n):
    phone = input().strip()
    freq[phone] = freq.get(phone, 0) + 1

answer = 0
for count in freq.values():
    if count == 3:
        answer += 1

print(answer)