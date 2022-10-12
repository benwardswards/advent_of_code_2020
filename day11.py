from copy import deepcopy
from rich import print
from rich import pretty
from rich import traceback
from dataclasses import dataclass

pretty.install()
traceback.install()

with open("day11.txt") as file:
    ferry = file.read()

test_ferry = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


# @dataclass
class Seat_predict:
    ferry_seats = list(list())
    n_row = 0
    n_col = 0

    def __init__(self, ferry_str: str):
        self.ferry_seats = [[c for c in line] for line in ferry_str.splitlines()]
        self.n_row = len(self.ferry_seats)
        self.n_col = len(self.ferry_seats[0])
        print(f"{self.n_row=}{self.n_col=} ")
        print(self)

    def __repr__(self):
        return "".join(("".join(list(l)) + "\n" for l in self.ferry_seats))

    def next_seat(self, row, col):
        full = 0

        spot = self.ferry_seats[row][col]

        for i in range((row - 1), (row + 2)):
            for j in range((col - 1), (col + 2)):
                if 0 <= i < self.n_row and 0 <= j < self.n_col:
                    seat = self.ferry_seats[i][j]

                    if seat == "#":
                        full += 1

        # print(f"{spot=}, {full=}, {empty=} ")
        if spot == ".":
            return "."

        if spot == "L":
            if full == 0:
                return "#"
            else:
                return "L"

        if spot == "#":
            if full >= 5:
                return "L"
            else:
                return "#"

    def taken(self, row, col, direction):
        """ "counts the number of emty seats that can be seen"""
        full = 0
        for i in range(1, max(self.n_row, self.n_col) // 2 + 1):
            irow = row - i * direction[0]
            icol = col - i * direction[1]
            print(f"{i=}, {irow=}, {icol=}, {direction=}, {row=}, {col=}")
            if 0 <= irow < self.n_row and 0 <= icol < self.n_col:
                if self.ferry_seats[irow][icol] == "#":
                    full += 1
                    break
                if self.ferry_seats[irow][icol] == "L":
                    break
        return full

    def next_seat_B(self, row, col):
        full: int = 0
        full2: int = 0
        spot = self.ferry_seats[row][col]
        for ud in [-1, 0, 1]:
            for rl in [-1, 0, 1]:
                if not (ud == 0 and rl == 0):
                    full2 += self.taken(row, col, [ud, rl])
        # case1 up

        for irow in range(0, row)[::-1]:
            if self.ferry_seats[irow][col] == "#":
                full += 1
                break
            if self.ferry_seats[irow][col] == "L":
                break

        # case upright
        for irow in range(0, row)[::-1]:
            icol = col + row - irow
            if 0 <= icol < self.n_col:
                if self.ferry_seats[irow][icol] == "#":
                    full += 1
                    break
                if self.ferry_seats[irow][icol] == "L":
                    break

        # case upleft

        for irow in range(0, row)[::-1]:
            icol = col - row + irow
            if 0 <= icol < self.n_col:
                if self.ferry_seats[irow][icol] == "#":
                    full += 1
                    break
                if self.ferry_seats[irow][icol] == "L":
                    break

        # case Down
        for irow in range(row + 1, self.n_row):
            if self.ferry_seats[irow][col] == "#":
                full += 1
                break
            if self.ferry_seats[irow][col] == "L":
                break

        # left
        for icol in range(0, col)[::-1]:
            if self.ferry_seats[row][icol] == "#":
                full += 1
                break
            if self.ferry_seats[row][icol] == "L":
                break

        # right
        for icol in range(col + 1, self.n_col):
            if self.ferry_seats[row][icol] == "#":
                full += 1
                break
            if self.ferry_seats[row][icol] == "L":
                break

        # down right
        for irow in range(row + 1, self.n_row):
            icol = col + irow - row
            if 0 <= icol < self.n_col:
                if self.ferry_seats[irow][icol] == "#":
                    full += 1
                    break  # down left
                if self.ferry_seats[irow][icol] == "L":
                    break

        # down left
        for irow in range(row + 1, self.n_row):
            icol = col - irow + row
            if 0 <= icol < self.n_col:
                if self.ferry_seats[irow][icol] == "#":
                    full += 1
                    break  # down left
                if self.ferry_seats[irow][icol] == "L":
                    break
        # print(f"{spot=}, {full=}, {self.n_row=} ")

        assert full == full2, print(full, full2)
        if spot == ".":
            return "."

        elif spot == "L":
            if full == 0:
                return "#"
            else:
                return "L"

        elif spot == "#":
            if full >= 5:
                return "L"
            else:
                return "#"

        else:
            raise NotImplementedError("can't get here")

    def stabilize(self, part="part_a"):
        if part == "part_a":
            part_f = self.next_seat
        else:
            part_f = self.next_seat_B
            print("using nextseatb")
        count = 0
        while True:
            count += 1
            temp = [
                [part_f(row, col) for col in range(self.n_col)]
                for row in range(self.n_row)
            ]
            if temp == self.ferry_seats:
                break
            print(self)
            self.ferry_seats = temp

        print(self)
        print(f"{count=}")
        return sum(
            1 if "#" == seat else 0 for line in self.ferry_seats for seat in line
        )


my_test_ferry = Seat_predict(test_ferry)

# print(my_test_ferry.stabilize())

my_ferry = Seat_predict(ferry)

# print(my_ferry.stabilize())

test_ferry3 = """LL#LL
#LLL#
#L#L#
#LLL# 
#L#L#
"""

my_test_ferry3 = Seat_predict(test_ferry3)
print(my_test_ferry3.next_seat_B(2, 2))
print(my_test_ferry.stabilize(part="part_b"))
# print(my_ferry.stabilize(part="part_b"))
