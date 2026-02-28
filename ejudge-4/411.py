import json

def merge(source, patch):
   result = {}

   for key, value in source.items():
      if key in patch:
         patch_value = patch[key]
         if patch_value is None:
            continue

         if isinstance(value, dict) and isinstance(patch_value, dict):
            result[key] = merge(value, patch_value)
         else:
            result[key] = patch_value
      else:
         result[key] = value

   for key, value in patch.items():
      if key not in source:
         if value is not None:
            result[key] = value

   return result

source = json.loads(input())
patch = json.loads(input())

print(json.dumps(merge(source, patch), sort_keys=True, separators=(',', ':')))

# {"user":{"name":"Ann","age":20},"active":true}
# {"user":{"age":21},"active":false}