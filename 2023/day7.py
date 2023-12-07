import re
from aoc import get_input
from pprint import pprint

input = get_input(7, 2023).strip()
# input = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483"""

cards = "AKQJT98765432."
cards2 = "AKQT98765432J."
cards = "".join(reversed([i for i in cards2]))


def score(s):
    return cards.index(s)


def five(s):
    for i in s:
        if i != s[0]:
            return False
    return score(s[0])


def four(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    if any([d == 4 for d in d.values()]):
        sum = 0
        for key, value in d.items():
            if value == 4:
                sum += 2 ** 15 * score(key)
            else:
                sum += 2 ** score(key)
        return sum
    return False


def full(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    if set(d.values()) == {2, 3}:
        items = list(d.items())
        items.sort(key=lambda x: x[1])
        return score(items[0][0]) + 2 ** 6 * score(items[1][0])
    return False


def three(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    if any([d == 3 for d in d.values()]):
        sum = 0
        for key, value in d.items():
            if value == 3:
                sum += score(key) * 2 ** 15
            else:
                sum += 2 ** score(key)
        return sum
    return False


def twopair(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    if list(d.values()).count(2) == 2:
        sum = 0
        for key, value in d.items():
            if value == 2:
                sum += 2 ** (2 * score(key))
            else:
                sum += 2 ** score(key)
        return sum
    return False


def onepair(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    if any([d == 2 for d in d.values()]):
        sum = 0
        for key, value in d.items():
            if value == 2:
                sum += score(key) * 2 ** 15
            else:
                sum += 2 ** score(key)
        return sum
    return False


def high(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    if len(d) == 5:
        return sum([2 ** score(i) for i in s])


def classify(s):
    if five(s):
        return 6, five(s)
    if four(s):
        return 5, four(s)
    if full(s):
        return 4, full(s)
    if three(s):
        return 3, three(s)
    if twopair(s):
        return 2, twopair(s)
    if onepair(s):
        return 1, onepair(s)
    if high(s):
        return 0, high(s)
    print('wat')


from functools import cmp_to_key


def card_sort(a, b):
    if a[0][0] == b[0][0]:
        for i, j in zip(a[1][0], b[1][0]):
            si, sj = score(i), score(j)
            if si == sj:
                continue
            if si > sj:
                return -1
            return 1
    if a[0][0] > b[0][0]:
        return -1
    return 1


split_cards = [s.split() for s in input.split("\n")]

scores = [(classify(s), (s, score)) for s, score in split_cards]


scores.sort(key=cmp_to_key(card_sort))
scores.reverse()

pprint(scores)

print(sum([(i + 1) * int(s[1][1]) for i, s in enumerate(scores)]))
