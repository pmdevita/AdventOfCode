from aoc import get_input

input = get_input(2, 2023).strip()

ids = []
cube_results = []
for line in input.split("\n"):
    id, cubes = line.split(": ")
    id = int(id[5:])

    blue_min = 0
    green_min = 0
    red_min = 0

    is_valid = True
    turns = cubes.split("; ")
    for turn in turns:
        for cube in turn.split(", "):
            num, color = cube.split(" ")
            num = int(num)
            match color:
                case "blue":
                    is_valid = is_valid and num <= 14
                    blue_min = max(blue_min, num)
                case "green":
                    is_valid = is_valid and num <= 13
                    green_min = max(green_min, num)
                case "red":
                    is_valid = is_valid and num <= 12
                    red_min = max(red_min, num)

    cube_results.append(blue_min * red_min * green_min)
    if is_valid:
        ids.append(id)

print(sum(ids))
print(sum(cube_results))



