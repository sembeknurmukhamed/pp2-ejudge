n, numbers = int(input()), list(map(int, input().split()))

freq = {}
for num in numbers: freq[num] = freq.get(num, 0) + 1

most_frequent = min(freq.keys(), key=lambda x: (-freq[x], x))
print(most_frequent)