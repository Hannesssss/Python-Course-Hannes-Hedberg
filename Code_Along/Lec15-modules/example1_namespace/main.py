import os, sys

os.system("cls||clear")

print(f"{'='*30}main.py{'='*30}")

import module1

# code imported from another module is exectued when imported
# when module1.py is ran -> __name__ = "__main__"

# when importing a moduke - a reference will be created to sys.modules
print("globals namespace")
print(globals()["module1"])

print("sys.modules")
print(sys.modules["module1"])
# note __name__ is module1 when ran from outside of module1.oy
print(f"\n{'='*30}end main{'='*30}")

