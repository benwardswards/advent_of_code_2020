from rich import print
from rich import pretty
from rich import traceback
from itertools import combinations

# from dataclasses import dataclass

traceback.install()
pretty.install()
with open("day9.txt") as file:
    data: list[int] = [int(d) for d in file.read().splitlines()]

print(data)


testdata_str = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".splitlines()

testdata: list[int] = [int(d) for d in testdata_str]

print(testdata)


def preamble(data: list[int], length=5):
    for i in range(length, len(data) - 1):
        start_index = i - length
        previous = {a + b for a, b in combinations(data[start_index:i], 2)}
        # print(f"{i},{data[i]=},{data[(i-5):(i)]=}{previous}")
        if data[i] not in previous:
            print(f"{i+1}, {data[i]} not the sum of the privious{length}")

            return data[i]


test_nosum = preamble(testdata)

nosum = preamble(data, 25)
print(f"{nosum=}")


def preamble2(data: list[int], value: int):
    print(f"looking for {value}")
    for length in range(2, len(data) - 1):
        for i in range(length, len(data) - 1):
            start = i - length
            if value == sum(data[start:i]):
                sublist = data[start:i]
                print("found!")
                print(f"{i=}, {length=},{sublist=}")

                return min(sublist) + max(sublist)


assert preamble2(testdata, test_nosum) == 62
print(
    f"The sum of min and max of the sublist that adds to value is {preamble2(data, nosum)}"
)
