import re

s = int(input())
s2 = input()
a = ["jolteon", "flareon", "umbreon", "leafeon", "glaceon", "sylveon"]
if len(s2) == 6:
    print("espeon")
elif len(s2) == 8:
    print("vaporeon")
else:
    for i in a:
        if re.match(s2, i, re.I):
            print(i)
