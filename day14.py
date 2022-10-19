from dataclasses import dataclass, field
from itertools import zip_longest

TESTDATA_STR = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
from rich import traceback, pretty, print

pretty.install()
traceback.install()

from pathlib import Path

print("data:")
DATA_STR = Path("day14.txt").read_text()


def parse(data_str: str):
    return [d.split(" = ") for d in data_str.splitlines()]


@dataclass
class Bitmask:
    mem: dict[int, int]
    instrunctions: list[str]
    mask: str

    def __init__(self, instructions: str):
        self.instrunctions = parse(instructions)
        self.mem = dict()

    def run(self):
        for ins, value in self.instrunctions:
            if ins == "mask":
                # print(ins, value)
                self.mask = list(value)[::-1]

            elif ins[:3] == "mem":
                reverse_digits = list(bin(int(value)))[2:][::-1]
                # print(value, reverse_digits)
                gen = zip_longest(reverse_digits, self.mask, fillvalue="0")
                out = []
                for digit, mask in gen:
                    # print(digit, mask)
                    match mask:
                        case "X":
                            out.append(digit)
                        case "0":
                            out.append("0")
                        case "1":
                            out.append("1")
                        case _:
                            raise ValueError("invalid mask")
                result = int("".join(out[::-1]), 2)
                address = int(ins[4:-1])
                # print(f"{result=},{address=}")
                self.mem[address] = result
            else:
                raise NotImplemented(" invalid insturction")
        # print(self.mem)
        print(f"sum = {sum(self.mem.values())}")


bitmask_test = Bitmask(TESTDATA_STR)
bitmask_test.run()

bitmask = Bitmask(DATA_STR)
bitmask.run()


def base10(base2_str: str) -> int:
    """converts a base 2 string to an int  base 10"""
    return int(base2_str, 2)


@dataclass
class BitmaskB:
    mem: dict[int, int]
    instrunctions: list[str]
    mask: str

    def __init__(self, instructions: str):
        self.instrunctions = parse(instructions)
        self.mem = dict()

    @staticmethod
    def combinations(digits: list[str]) -> list[int]:
        """returns all the addresss when you convert X to 0 and 1s and convert to int from binary"""
        strings_out = [""]
        for digit in digits:
            if digit in ["0", "1"]:
                strings_out = [st + digit for st in strings_out]
            else:
                strings_out = [st + "0" for st in strings_out] + [
                    st + "1" for st in strings_out
                ]

        return [base10(string) for string in strings_out]

    def run(self):
        for ins, value in self.instrunctions:
            if ins == "mask":
                self.mask = list(value)[::-1]
            elif ins.startswith("mem"):
                # print(value, reverse_digits)
                address = int(ins[4:-1])  # remove mem[]
                reverse_digits = list(bin(address))[2:][::-1]

                gen = zip_longest(reverse_digits, self.mask, fillvalue="0")
                out_digits = []
                for digit, mask in gen:
                    match mask:
                        case "X":
                            out_digits.append("X")
                        case "0":
                            out_digits.append(digit)
                        case "1":
                            out_digits.append("1")
                        case _:
                            raise ValueError("invalid mask")

                for address in self.combinations(out_digits[::-1]):
                    self.mem[address] = int(value)
            else:
                raise NotImplemented(" invalid insturction")
        print(f"The number of unquie adresses is: {len(self.mem)}")
        print(f"sum for part B= {sum(self.mem.values())}")


TESTDATA2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""

bitmaskB = BitmaskB(TESTDATA2)
print(bitmaskB.combinations(["X", "1", "1", "0", "1", "X"]))
print(bitmaskB.combinations(["1", "X", "0", "X", "X"]))
bitmaskB.run()

bitmaskB = BitmaskB(DATA_STR)
bitmaskB.run()
