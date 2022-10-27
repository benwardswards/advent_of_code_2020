from pathlib import Path
from rich import traceback, print
from itertools import pairwise

data = Path("day18.txt").read_text()


class AddMux:
    @staticmethod
    def nobrackets(in_str: str) -> int:
        """in_str: a string like 1+2*3+4 with no brackets
        excutes left to right multiples and adds with no operator presdence
        returns the computation
        """

        op_num_list: list[str] = in_str.split(" ")

        cumlative = int(op_num_list[0])
        for op, num in list(pairwise(op_num_list))[1:]:
            if op == "+":
                cumlative += int(num)
            elif op == "*":
                cumlative *= int(num)
        return cumlative

    @staticmethod
    def nobrackets_part2(in_str: str) -> int:
        """in_str: a string of 1+2*3+4 with no brackets
        excutes adds before multiples returns the computation
        """

        op_num_list: list[str] = in_str.split(" ")
        # print(op_num_list)

        cumlative: int = int(op_num_list[0])
        multiples: int = 1

        # exacute all adds first!
        for op, num in list(pairwise(op_num_list))[1:]:
            if op == "+":
                cumlative += int(num)
            elif op == "*":
                # excute multiples after
                multiples *= int(cumlative)
                cumlative = int(num)
        multiples *= int(cumlative)

        return multiples

    @classmethod
    def brackets(cls, in_str: str) -> int:
        """in_str: string of adds with brackets 1+2*(6+9) excutle brackets with left to right
        extracts sublists with outer bracket removed and rersively calls it self.
        if the sublist has no brackets call no_brackets on sublist"""

        i = 0
        # print(in_str)
        while i < len(in_str):
            """extract sub list inside brackets and recusrivly apply the function on it."""
            if in_str[i] == "(":
                j = i + 1
                n_brackets: int = 0  # counter to find closing brackets e.g. ((5+3)+3)
                while True:
                    if in_str[j] == ")" and n_brackets == 0:

                        in_str = (
                            in_str[:i]
                            + str(cls.brackets(in_str[(i + 1) : j]))
                            + in_str[(j + 1) :]
                        )
                        break
                    elif in_str[j] == "(":
                        n_brackets += 1
                    elif in_str[j] == ")":
                        n_brackets -= 1
                    elif n_brackets < 0:
                        raise ValueError(" bracket counter can't be negative")
                    j += 1
            i += 1
        # there are no brackets in in_str so call no brackets to return result.
        return cls.nobrackets(in_str)

    @classmethod
    def brackets_part2(cls, in_str):
        """like brackets but does adds before muptlipes"""
        i = 0
        # print(in_str)
        while i < len(in_str):
            if in_str[i] == "(":
                j = i + 1
                n_brackets = 0
                while True:
                    if in_str[j] == ")" and n_brackets == 0:

                        in_str = (
                            in_str[:i]
                            + str(cls.brackets_part2(in_str[(i + 1) : j]))
                            + in_str[(j + 1) :]
                        )
                        break
                    elif in_str[j] == "(":
                        n_brackets += 1
                    elif in_str[j] == ")":
                        n_brackets -= 1
                    elif n_brackets < 0:
                        raise ValueError("can't be negative")
                    j += 1
            i += 1

        return cls.nobrackets_part2(in_str)


testdata = """1 + 2 * 3 + 4 * 5 + 6"""
testdata2 = "2 * 3 + (4 * 5)"
testdata3 = "1 + (2 * 3) + (4 * (5 + 6))"
testdata4 = "5 + (8 * 3 + 9 + 3 * 4 * 3)"
testdata5 = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
testdata6 = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
assert 231 == AddMux.nobrackets_part2(testdata)
print("testdata2 46 =", AddMux.brackets_part2(testdata2))
print("testdata3 51 =", AddMux.brackets_part2(testdata3))
print("testdata4 1445 =", AddMux.brackets_part2(testdata4))
print("testdata5 669060 =", AddMux.brackets_part2(testdata5))
print("testdata6 23340 =", AddMux.brackets_part2(testdata6))

print("done")


total = sum(AddMux().brackets_part2(line) for line in data.splitlines())

print(f"{total=} part 2")
print("part1 test data:")

print("testdata 71=", AddMux.nobrackets(testdata))
print("testdata 71=", AddMux.brackets(testdata))

print("testdata2 26 =", AddMux.brackets(testdata2))
print("testdata3 51 =", AddMux.brackets(testdata3))
print("testdata4 437 =", AddMux.brackets(testdata4))
assert 12240 == AddMux.brackets(testdata5)
print("testdata6 13632 =", AddMux.brackets(testdata6))

total = sum(AddMux().brackets(line) for line in data.splitlines())

print(f"{total=} part 1")

print("done")
