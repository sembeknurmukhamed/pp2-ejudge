import json
import re

# Read input
data = json.loads(input())
n = int(input())

for _ in range(n):
    query = input()

    tokens = []
    for match in re.finditer(r'([a-zA-Z_]\w*)|\[(\d+)\]', query):
        if match.group(1) is not None:
            tokens.append(match.group(1))
        else:
            tokens.append(int(match.group(2))) 

    current = data
    found = True

    for token in tokens:
        try:
            current = current[token]
        except (KeyError, IndexError, TypeError):
            found = False
            break

    if found:
        print(json.dumps(current, separators=(',', ':')))
    else:
        print("NOT_FOUND")
