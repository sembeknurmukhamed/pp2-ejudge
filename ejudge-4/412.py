import json

def compare(obj1, obj2, path=""):
   differences = []

   keys = set(obj1.keys()) | set(obj2.keys())

   for key in keys:
      new_path = f"{path}.{key}" if path else key

      in1 = key in obj1
      in2 = key in obj2

      if not in1:
         differences.append(f"{new_path} : <missing> -> {json.dumps(obj2[key], separators=(',', ':'))}")
      elif not in2:
         differences.append(f"{new_path} : {json.dumps(obj1[key], separators=(',', ':'))} -> <missing>")
      else:
         val1 = obj1[key]
         val2 = obj2[key]

         if isinstance(val1, dict) and isinstance(val2, dict):
            differences.extend(compare(val1, val2, new_path))
         else:
            if val1 != val2:
               differences.append(
                        f"{new_path} : "
                        f"{json.dumps(val1, separators=(',', ':'))} -> "
                        f"{json.dumps(val2, separators=(',', ':'))}"
                    )

   return differences

obj1 = json.loads(input())
obj2 = json.loads(input())

diffs = compare(obj1, obj2)

if not diffs:
    print("No differences")
else:
    for line in sorted(diffs):
        print(line)