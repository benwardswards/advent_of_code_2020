from dataclasses import dataclass
from itertools import product
from rich import print, pretty, traceback

pretty.install()
traceback.install()

with open("day11.txt", encoding="utf-8") as file:
    FERRY = file.read()

TEST_FERRY = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


@dataclass
class Dir:
    # simple int vector
    row: int
    col: int


class SeatPredict:
    """A class for figuring out where people will sit on a ferry"""

    ferry_seats: list[list[str]]
    n_row: int = 0
    n_col: int = 0

    def __init__(self, ferry_str: str):
        self.ferry_seats = [list(line) for line in ferry_str.splitlines()]
        self.n_row = len(self.ferry_seats)
        self.n_col = len(self.ferry_seats[0])
        print(f"{self.n_row=}{self.n_col=} ")
        print(self)

    def __repr__(self):
        return "".join(("".join(list(li)) + "\n" for li in self.ferry_seats))

    def next_seat(self, row: int, col: int) -> str:
        """Returns the next seat for ferry_A given a location row,col"""
        full: int = (
            0  # counter for the number of full seats inthe circle
            # round row,col
        )

        spot: str = self.ferry_seats[row][col]  # extracting type of seat

        # check the cells around row,col for how many #'s
        # check boundaries
        for i_row, j_col in product([-1, 0, 1], [-1, 0, 1]):
            cond_1 = 0 <= row + i_row < self.n_row
            cond_2 = 0 <= col + j_col < self.n_col
            if cond_1 and cond_2:
                seat = self.ferry_seats[row + i_row][col + j_col]
                if seat == "#":
                    full += 1

        # print(f"{spot=}, {full=}, {empty=} ")
        match spot, full:
            case ".", _:
                return "."
            case "L", 0:
                return "#"
            case "#", 0 | 1 | 2 | 3 | 4:
                return "#"
            case _:
                return "L"

    def taken(self, row: int, col: int, direction: Dir):
        """counts the number of"""
        full: int = 0
        seats_in_direction = max(self.n_row, self.n_col) // 2 + 1
        for i in range(1, seats_in_direction):
            irow = row - i * direction.row
            icol = col - i * direction.col
            # print(f"{i=}, {irow=}, {icol=}, {direction=}, {row=}, {col=}")
            valid_seat = 0 <= irow < self.n_row and 0 <= icol < self.n_col
            if valid_seat:
                if self.ferry_seats[irow][icol] == "#":
                    # found a full seat
                    full += 1
                    break
                if self.ferry_seats[irow][icol] == "L":
                    # found an empyt seat so stop looking
                    break
        return full

    def next_seat_B(self, row, col):
        full: int = 0
        spot = self.ferry_seats[row][col]
        for col_dir in [-1, 0, 1]:
            for row_dir in [-1, 0, 1]:
                if not (row_dir == 0 and col_dir == 0):
                    full += self.taken(row, col, Dir(col_dir, row_dir))

        match spot, full:
            case ".", _:
                return "."
            case "L", 0:
                return "#"
            case "#", 0 | 1 | 2 | 3 | 4:
                return "#"
            case _:
                return "L"

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
            # print(self)
            self.ferry_seats = temp

        print(self)
        print(f"{count=}")
        return sum(
            1 if "#" == seat else 0 for line in self.ferry_seats for seat in line
        )


if __name__ == "__main__":

    my_test_ferry = SeatPredict(TEST_FERRY)

    result = my_test_ferry.stabilize()
    print("part a test should be 37== ", result)
    assert result == 37
    my_ferry = SeatPredict(FERRY)

    result = my_ferry.stabilize()
    print(f"part a data: {result} which should be 2249")
    assert result == 2249
    TEST_FERRY3 = """LL#LL
    #LLL#
    #L#L#
    #LLL#
    #L#L#
    """

    my_test_ferry3 = SeatPredict(TEST_FERRY3)
    print(my_test_ferry3.next_seat_B(2, 2))

    my_test_ferry_b = SeatPredict(TEST_FERRY)
    result_test_b = my_test_ferry_b.stabilize(part="part_b")
    print(f"{result_test_b=} ")
    assert result_test_b == 26

    my_ferry_b = SeatPredict(FERRY)
    print(my_ferry_b.stabilize(part="part_b"))
