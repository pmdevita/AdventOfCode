from aoc import get_input

input = get_input(3, 2023).strip()

schem = input.split("\n")

part_nums = []
gears = {}

def is_symbol(sym):
    return not sym.isdigit() and not sym == "."


for y, line in enumerate(schem):
    line_gears = []
    def gear(x, y):
        if schem[y][x] != "*":
            return
        line_gears.append(y * len(line) + x)

    number = ""
    has_sym = False
    for x, d in enumerate(line):
        if not d.isdigit():
            if has_sym and number:
                number = int(number)
                part_nums.append(number)
                for g in set(line_gears):
                    if g not in gears:
                        gears[g] = []
                    gears[g].append(number)
            number = ""
            has_sym = False
            line_gears = []
            continue
        number += d
        # X
        if x > 0:
            gear(x - 1, y)
            has_sym = has_sym or is_symbol(line[x - 1])
        if x < (len(line) - 1):
            gear(x + 1, y)
            has_sym = has_sym or is_symbol(line[x + 1])
        # Y
        if y > 0:
            gear(x, y - 1)
            has_sym = has_sym or is_symbol(schem[y - 1][x])
        if y < len(schem) - 1:
            gear(x, y + 1)
            has_sym = has_sym or is_symbol(schem[y + 1][x])
        # upper left
        if x > 0 and y > 0:
            gear(x - 1, y - 1)
            has_sym = has_sym or is_symbol(schem[y - 1][x - 1])
        # upper right
        if x < len(line) - 1 and y > 0:
            gear(x + 1, y - 1)
            has_sym = has_sym or is_symbol(schem[y - 1][x + 1])
        # down left
        if x > 0 and y < len(schem) - 1:
            gear(x - 1, y + 1)
            has_sym = has_sym or is_symbol(schem[y + 1][x - 1])
        # down right
        if x < len(line) - 1 and y < len(schem) - 1:
            gear(x + 1, y + 1)
            has_sym = has_sym or is_symbol(schem[y + 1][x + 1])

    if has_sym and number:
        number = int(number)
        part_nums.append(number)
        for g in line_gears:
            if g not in gears:
                gears[g] = []
            gears[g].append(number)


print(sum(part_nums))
good_gears = [value for key, value in gears.items() if len(value) == 2]
gear2 = [i * j for i, j in good_gears]
print(sum(gear2))
