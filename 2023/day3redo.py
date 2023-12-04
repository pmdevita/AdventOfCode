from aoc import get_input

input = get_input(3, 2023).strip()

schem = input.split("\n")
line_length = len(schem[0])
blank_line = "".join(["." for i in range(line_length)])
schem.insert(0, blank_line)
schem.append(blank_line)

for i in range(len(schem)):
    schem[i] = "." + schem[i] + "."


part_nums = []
gears = {}


def is_symbol(sym):
    return not sym.isdigit() and not sym == "."


for y, line in enumerate(schem):
    line_gears = []
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

        for sym_x in [x - 1, x, x + 1]:
            for sym_y in [y - 1, y, y + 1]:
                if sym_y == 0 and sym_x == 0:
                    continue
                has_sym = has_sym or is_symbol(schem[sym_y][sym_x])
                if schem[sym_y][sym_x] != "*":
                    continue
                line_gears.append(sym_y * len(line) + sym_x)

print(sum(part_nums))
good_gears = [value for key, value in gears.items() if len(value) == 2]
gear2 = [i * j for i, j in good_gears]
print(sum(gear2))
