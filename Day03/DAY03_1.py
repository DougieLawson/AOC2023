def read(filename) -> list[str]:
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]
        
import re

numbersRegex = re.compile(r'\d+')

lines = read('DAY03.txt')

numbers = []
lineMap = {}
for i, line in enumerate(lines):
    for item in re.finditer(numbersRegex, line):
        idx = len(numbers)
        numbers.append(int(item.group()))
        for j in range(item.start(), item.end()):
            lineMap[i,j] = idx
    
symbolRegex = re.compile(r'[^\.\d]')

found = set()
for i, line in enumerate(lines):
    for item in re.finditer(symbolRegex, line):
        for l in range(i-1, i+2):
            for c in range(item.start()-1, item.start()+2):
                if lineMap.get((l,c)) != None:
                    found.add(lineMap[l,c])

print(sum([numbers[i] for i in found]))