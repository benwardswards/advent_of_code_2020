from dataclasses import dataclass, field
from rich import print, pretty, traceback

pretty.install()
traceback.install()

with open("day12.txt", encoding="utf-8") as file:
    FERRY = file.read()

TEST_FERRY = """F10
N3
F7
R90
F11"""


@dataclass
class Instruc:
    number: int
    dir: str

    def __init__(self, in_str: str):
        self.dir, temp = in_str[0], int(in_str[1:])
        match self.dir:
            case "R":
                self.number = temp // 90
            case "L":
                self.number = -temp // 90
            case "N" | "W" | "E" | "S" | "F":
                self.number = temp
            case _:
                raise TypeError(f"invalid {self.dir} ")


assert Instruc("R90").number == 1
assert Instruc("R90").dir == "R"
assert Instruc("R180").number == 2
assert Instruc("L180").number == -2


def go_right(direction, value):
    dir_list = "N E S W".split()
    out_index = (dir_list.index(direction) + value) % 4
    return dir_list[out_index]


assert go_right("N", 0) == "N"
assert go_right("N", 1) == "E"
assert go_right("N", -1) == "W"
assert go_right("N", 2) == "S"
assert go_right("E", -1) == "N"


@dataclass
class Ferry:
    instruction_list: list[Instruc] = field(repr=False)
    direction: str = "E"
    east: int = 0
    north: int = 0

    def __init__(self, instruction_list):
        self.instruction_list = [Instruc(ins) for ins in instruction_list.splitlines()]

    def next_dir(self, instruction: Instruc):
        """turn the ferry"""

        self.direction = go_right(self.direction, instruction.number)

    def move(self, instruction: Instruc):
        "move the ferry"
        match instruction.dir:
            case "N":
                self.north += instruction.number
            case "S":
                self.north -= instruction.number
            case "E":
                self.east += instruction.number
            case "W":
                self.east -= instruction.number

            case "F":
                self.move(Instruc(self.direction + str(instruction.number)))
            case _:
                raise TypeError(f"invalid direction{instruction}")

    def simulate(self):
        for instruction in self.instruction_list:
            if instruction.dir in set(("R", "L")):
                self.next_dir(instruction)
            else:
                self.move(instruction)
            # print(f"{instruction},{self.direction},{self.east=},{self.north=}")
        print(f"the total distance is {self.north,self.east}")
        print(f"The manhattan distance is {abs(self.north)+abs(self.east)}")


testferry = Ferry(TEST_FERRY)
print("At the starting: ", testferry)
testferry.simulate()

ferry = Ferry(FERRY)
print(ferry)
ferry.simulate()


@dataclass
class FerryB:
    instruction_list: list[Instruc] = field(repr=False)
    wp_east: int = 10
    wp_north: int = 1
    east: int = 0
    north: int = 0

    def __init__(self, instruction_list):
        self.instruction_list = [Instruc(ins) for ins in instruction_list.splitlines()]

    def next_dir(self, instruction: Instruc):
        """turn the ferry"""

        for _ in range(instruction.number % 4):
            # number of turns, 90 degree rotion to the right
            self.wp_east, self.wp_north, = (
                self.wp_north,
                -self.wp_east,
            )

    def move(self, instruction: Instruc):
        "move the ferry"
        match instruction.dir:
            case "N":
                # move the waypoint
                self.wp_north += instruction.number
            case "S":
                self.wp_north -= instruction.number
            case "E":
                self.wp_east += instruction.number
            case "W":
                self.wp_east -= instruction.number
            case "F":
                # move in the direction of the waypoint
                self.north += instruction.number * self.wp_north
                self.east += instruction.number * self.wp_east
            case _:
                raise TypeError(f"invalid direction{instruction}")

    def simulate(self):
        for instruction in self.instruction_list:
            if instruction.dir in ["R", "L"]:
                self.next_dir(instruction)
            else:
                self.move(instruction)
            # print(f"{instruction}")
            # print(self)
        print(f"the total distance for part B is {self.north,self.east}")
        print(f"The manhattan distance is {abs(self.north)+abs(self.east)}")


testferry = FerryB(TEST_FERRY)
print(testferry)
testferry.simulate()

ferry = FerryB(FERRY)
print(ferry)
ferry.simulate()
