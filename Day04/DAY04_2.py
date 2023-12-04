from collections import defaultdict
d = open("DAY04.txt").read().strip()
lines = d.split('\n')
answer = 0
N = defaultdict(int)
for i, line in enumerate(lines):
    N[i] += 1
    start, last = line.split('|')
    id, winners = start.split(':')
    win_nums = [int(x) for x in winners.split()]
    entry_nums = [int(x) for x in last.split()]
    val = len(set(win_nums) & set(entry_nums))
    
    if val > 0:
        answer += 2**(val-1)
    for j in range(val):
        N[i+1+j] += N[i]

print(answer)
print(sum(N.values()))