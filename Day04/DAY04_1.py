d = open("DAY04.txt").read().strip()
lines = d.split('\n')
answer = 0
for line in lines:
    start, last = line.split('|')
    id, winners = start.split(':')
    win_nums = [int(x) for x in winners.split()]
    entry_nums = [int(x) for x in last.split()]
    val = len(set(win_nums) & set(entry_nums))
    
    if val > 0:
        answer += 2**(val-1)
    print(answer, id, win_nums, entry_nums, val, 2**val)

print(answer)