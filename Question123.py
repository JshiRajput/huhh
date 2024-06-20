

quote = "Brave Sir Robin ran away. Bravely ran away away. When danger reared it's ugly head, he bravely turned his tail and fled. Brave Sir Robin turned about and gallantly he chickened out..."
x = {}

for i in quote:
    if i in x:
        x[i] += 1
    else:
        x[i] = 1
print(x)








def mysterious_function(n):
    if n <= 1:
        return 1
    return n * mysterious_function(n - 1)

a = int(input("enter a number"))
for i in range(1,a+1):
    print(mysterious_function(i))








import re

def split_string(s):
    parts = re.findall(r'\d+|[a-zA-Z]+|[^a-zA-Z\d]+', s)

    result = [int(part) if part.isdigit() else part for part in parts]

    return result
x = "Nobody0expects42the2048Spanish1492Inquisition!"
print(split_string(x))
