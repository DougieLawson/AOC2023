import re
total = 0
num = "one two three four five six seven eight nine".split()
regex = "(?=(" + "|".join(num) + "|\\d))"

def f(x):
    if x in num:
        return str(num.index(x) + 1)
    return x
    
for record in open("DAY01.txt"):
    digits = [*map(f, re.findall(regex,record))]
    total += int(digits[0] + digits[-1])
    
print(total)