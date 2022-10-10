from rich import print
from rich import pretty
from rich import traceback
from itertools import pairwise
from collections import Counter
from collections import defaultdict

pretty.install()
traceback.install()

# from dataclasses import dataclass

with open("day10.txt") as file:
    string: str = file.read()

# print(string)

test_string = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

test_string2 = """16
10
15
5
1
11
7
19
6
12
4"""


def circuit(data_str: str) -> int:
    data: list[int] = [int(d) for d in data_str.splitlines()]

    jump_combinations: dict[int:int] = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7}
    # number of combinations a streak of ones has using jump circuits

    data.append(0)  # start with zero volatage
    data.append(3 + max(data))  # end with 3+max voltage
    data.sort()
    data_diff = [y - x for x, y in pairwise(data)]

    jumps = Counter(data_diff)

    streaks: defaultdict[int, int] = defaultdict(int)
    # dict  length of streak : number of these streaks of one

    streak_of_ones = 0
    number_circuits = 1
    for value in data_diff:
        # caculates the length and number of streaks of ones' in diff
        if value == 1:
            streak_of_ones += 1
        else:
            streaks[streak_of_ones] += 1
            number_circuits *= jump_combinations[streak_of_ones]
            # streak_of_ones muptlies to give a certain number of conbinations
            streak_of_ones = 0

    print(f"{data_diff=},{jumps=}")
    print(f"part1: {jumps[3] * jumps[1]=},")
    print(f"{streaks=}")
    print(f"part2: {number_circuits=}")
    return jumps[3] * jumps[1]


print("___________testdata2")
jumpnumber = circuit(test_string2)
print("___________testadata")
jumpnumber = circuit(test_string)
print("___________data")
jumpnumber = circuit(string)
