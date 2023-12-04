import re

from aoc import get_input

input = get_input(4, 2023).strip()

header_len = len("Card   1:")
total = 0
total_mult = 0

card_mult = [1 for i in range(len(input.split("\n")))]
card_mult[0] = 1

def get_nums(s):
    return [int(i.strip()) for i in re.findall(" \d+", s)]


for i, card in enumerate(input.split("\n")):
    sides = card[header_len:]
    winning, mine = sides.split("|")
    winning = get_nums(winning)
    mine = get_nums(mine)
    winning = set(winning)
    mine = set(mine)
    print(len(winning.intersection(mine)))
    matches = winning.intersection(mine)
    if len(matches) > 0:
        for j in range(len(matches)):
            card_mult[i + j + 1] += card_mult[i]
        total += 2 ** (len(winning.intersection(mine)) - 1)
        total_mult = card_mult[i] * 2 ** (len(winning.intersection(mine)) - 1)

print(total)
print(sum(card_mult))
