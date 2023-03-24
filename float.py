import re
n = int(input())
for i in range(n):
    if re.match("^[+-]?[0-9]*\.[0-9]+$", input()):
        print(True)
    else:
        print(False)
