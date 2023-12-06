import re
from aoc import get_input

input = get_input(6, 2023).strip()

lines = input.split("\n")


def get_nums(s):
    return [int(i.strip()) for i in re.findall(r" \d+", s)]


times = get_nums(lines[0])
distances = get_nums(lines[1])
times2 = int("".join([str(t) for t in times]))
distances2 = int("".join([str(t) for t in distances]))


def verify(hold_time, time, distance):
    remaining_time = time - hold_time
    return distance < remaining_time * hold_time


def find_range(time, distance):
    min_time = time
    max_time = 0
    for i in range(time):
        if verify(i, time, distance):
            min_time = min(min_time, i)
            max_time = max(max_time, i)
    return max_time - min_time + 1


def find_range2(time, distance):
    min_time = time
    for i in range(time):
        if verify(i, time, distance):
            min_time = i
            break

    max_time = 0
    for i in range(time, 0, -1):
        if verify(i, time, distance):
            max_time = i
            break

    return max_time - min_time + 1


total = 1
numbers = []
for t, d in zip(times, distances):
    numbers.append(find_range(t, d))
    total *= find_range(t, d)
print(total)
print(find_range2(times2, distances2))
