from rich import print

# from dataclasses import dataclass

with open("day6.txt") as file:
    data = file.read().splitlines()


print(data)

testdata = """abc

a
b
c

ab
ac

a
a
a
a

b""".splitlines()

print(data)


def customs(data: list[str]):
    groups: list[set] = []
    letters: set = set()
    for line in data:
        if line == "":
            groups.append(letters)
            letters = set()
        else:
            letters |= set(line)
    groups.append(letters)
    return sum(len(group) for group in groups)


assert customs(testdata) == 11


print("total value", customs(data))


def customs2(data: list[str]) -> int:
    flag_first: bool = True

    groups = []
    letters = set()
    for line in data:
        if line == "":
            groups.append(letters)
            letters = set()
            flag_first = True
        else:
            if flag_first is True:
                letters = set(line)
                flag_first = False
            else:
                letters &= set(line)
    groups.append(letters)
    # print(list(len(group) for group in groups))
    return sum(len(group) for group in groups)


print(
    "total value of distinct letters that every group has in the test data",
    customs2(testdata),
)

assert customs2(testdata) == 6

print("total value of distinct letters that every group has", customs2(data))
