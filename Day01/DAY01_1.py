#!/usr/bin/python

total = 0
for x in open("./DAY01.txt"):
    digits = [ch for ch in x if ch.isdigit()]
    total += int(digits[0] + digits[-1])

print("Part 1: ", total)
