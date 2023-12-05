import re
from aoc import get_input

input = get_input(5, 2023).strip()

sections = input.split("\n\n")


def get_nums(s):
    return [int(i.strip()) for i in re.findall(r" \d+", s)]


def get_map(section):
    rules = []
    for line in section.split("\n")[1:]:
        nums = [int(i) for i in line.split(" ")]
        rules.append((nums[1], nums[0], nums[2]))
    rules.sort(key=lambda x: x[0])
    return rules


def translate_num(number: int, rules: list):
    for i, r in enumerate(rules):
        if r[0] <= number < r[0] + r[2]:
            return r[1] + (number - r[0])
    return number


def get_seed_locations(seeds):
    locations = []
    for seed in seeds:
        num = seed
        for map in maps:
            num = translate_num(num, map)
        locations.append(num)
    return locations


def find_paths(rules1: list, rules2: list):
    source_rules = rules1.copy()
    usable_r2 = set()
    while source_rules:
        r = source_rules.pop(0)
        matching = [r2 for r2 in rules2 if r[1] <= r2[0] < r[1] + r[2] or r2[0] <= r[1] < r2[0] + r2[2]]
        # Rule matches nothing, forwards through layer
        if not matching:
            usable_r2.add(r)
            continue

        r2 = matching[0]
        # Rewrite rule inner
        r_start = max(r[1], r2[0])
        r_end = min(r[1] + r[2], r2[0] + r2[2])
        rule = (r_start, r_start - r2[0] + r2[1], r_end - r_start)
        usable_r2.add(rule)

        if r[1] < r_start < r[1] + r[2]:
            source_rules.append((r[1], r[1], r_start - r[1]))

        if r[1] < r_end < r[1] + r[2]:
            source_rules.append((r_end, r_end, r[1] + r[2] - r_end))

    return list(usable_r2)


seeds = get_nums(sections[0][6:])

seeds2 = []
for i in range(0, len(seeds), 2):
    seeds2.append((0, seeds[i], seeds[i + 1]))

maps = [get_map(s) for s in sections[1:]]

locations = get_seed_locations(seeds)
locations.sort()
print(locations[0])

current = seeds2
for map in maps:
    current = find_paths(current, map)

current.sort(key=lambda x: x[1])

print(current[0][1])
