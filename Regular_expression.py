#Meta characters

import re

Text = "My Name Is Pranto"
pattern="[a-m]"

print(re.findall(pattern, Text))

x=re.findall("^M",Text)
if x:
    print("yes")
else:
    print("no")

x=re.findall("Pranto$",Text)
if x:
    print("yes")
else:
    print("no")
