from string import digits
from aoc import get_input

input = get_input(1, 2023).strip()


digits = [i for i in digits] + ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

word_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

values = []

for line in input.split("\n"):
    left_digit = None
    right_digit = None
    for left in range(len(line)):
        for digit in digits:
            if line[left:].startswith(digit):
                left_digit = digit
                break
        if left_digit:
            break
    for right in range(len(line), -1, -1):
        for digit in digits:
            if line[:right].endswith(digit):
                right_digit = digit
                break
        if right_digit:
            break

    if left_digit in word_digits:
        left_digit = str(word_digits.index(left_digit) + 1)

    if right_digit in word_digits:
        right_digit = str(word_digits.index(right_digit) + 1)

    values.append(int(left_digit + right_digit))

print(sum(values))
