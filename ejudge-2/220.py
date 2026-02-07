n, _dict = int(input()), {}
for i in range(n):
   cmd = input().split()
   if cmd[0] == "set": _dict[cmd[1]] = cmd[2]
   else:
      key = cmd[1]
      print(_dict.get(key, f"KE: no key {key} found in the document"))