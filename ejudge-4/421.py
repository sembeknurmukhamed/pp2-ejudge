import importlib

n = int(input())

for _ in range(n):
    module_path, attr_name = input().split()

    try:
        module = importlib.import_module(module_path)
    except ModuleNotFoundError:
        print("MODULE_NOT_FOUND")
        continue

    try:
        attr = getattr(module, attr_name)
    except AttributeError:
        print("ATTRIBUTE_NOT_FOUND")
        continue

    if callable(attr):
        print("CALLABLE")
    else:
        print("VALUE")