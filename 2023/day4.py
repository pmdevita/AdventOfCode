import re

from aoc import get_input

input = get_input(4, 2023).strip()

header_len = len("Card   1:")
total = 0

card_mult = [1 for i in range(len(input.split("\n")))]


def get_nums(s):
    return [int(i.strip()) for i in re.findall(r" \d+", s)]


for i, card in enumerate(input.split("\n")):
    sides = card[header_len:]
    winning, mine = sides.split("|")
    winning = set(get_nums(winning))
    mine = set(get_nums(mine))
    matches = len(winning.intersection(mine))
    if matches > 0:
        for j in range(matches):
            card_mult[i + j + 1] += card_mult[i]
        total += 2 ** (matches - 1)
        total_mult = card_mult[i] * 2 ** (matches - 1)

print(total)
print(sum(card_mult))
