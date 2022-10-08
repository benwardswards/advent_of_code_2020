from rich import print
from dataclasses import dataclass
from itertools import pairwise

with open("day5.txt") as file:
    data = file.read().splitlines()


# print(data)
testdata0 = "FBFBBFFRLR"
testdata1 = "BFFFBBFRRR"  #: row 70, rowumn 7, seat ID 567.
testdata2 = "FFFBBBFRRR"  #: row 14, rowumn 7, seat ID 119.
testdata3 = "BBFFBBFRLL"  #: row 102, rowumn 4, seat ID 820.


@dataclass
class Seat:
    minrow: int = 0
    maxrow: int = 127
    mincol: int = 0
    maxcol: int = 7

    def process(self, ticket: str):
        for letter in ticket:
            # print(letter, repr(self))
            if letter in "BF":
                newblock = (self.maxrow + self.minrow) // 2
                if letter == "B":
                    # print(letter, self.minrow, newblock, self.maxrow)
                    self.minrow = newblock + 1
                    self.maxrow = self.maxrow
                if letter == "F":
                    # print(letter, self.minrow, newblock, self.maxrow)
                    self.minrow = self.minrow
                    self.maxrow = newblock
            if letter in "RL":
                newblock = (self.maxcol + self.mincol) // 2
                if letter == "R":
                    # print(letter, self.mincol, newblock, self.maxcol)
                    self.mincol = newblock + 1
                    self.maxcol = self.maxcol
                if letter == "L":
                    # print(letter, self.mincol, newblock, self.maxcol)
                    self.mincol = self.mincol
                    self.maxcol = newblock
        self.id = self.minrow * 8 + self.maxcol
        print("id:", self.id, repr(self))
        assert self.mincol == self.maxcol
        assert self.minrow == self.maxrow

        return self.id


seat0 = Seat()
seat1 = Seat()
seat2 = Seat()
seat3 = Seat()
assert seat0.process(testdata0) == 357
assert seat1.process(testdata1) == 567
assert seat2.process(testdata2) == 119
assert seat3.process(testdata3) == 820


max_id = max(Seat().process(row) for row in data)

print(f"{max_id=}")


# part2

seats = [Seat().process(row) for row in data]
seats.sort()

print(seats)

print("The gaps in the list")
for seat1, seat2 in pairwise(seats):
    if seat2 - seat1 != 1:
        print(seat1, seat2)
