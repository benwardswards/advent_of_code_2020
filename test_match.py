from dataclasses import dataclass, field
from rich import print, traceback

traceback.install()


def func(x, y):
    """Test match case"""
    match x, y:
        case 0, _:
            print(f"{x=},{y=} first case ")
        case 1, 2:
            print(f"{x=},{y=} second case ")
        case 1, 6 | 3 | 4 | 5:
            print(f"{x=},{y=} 3 case ")
        case 2, 2:
            print(f"{x=},{y=} 4 case ")

        case _:
            print(f"{x=},{y=} 5 case ")


func(0, 1)
func(1, 2)
func(1, 5)

func(1, 1)

func(2, 2)


def response(input_):
    match input_:
        case 200, *input_:
            print(f"good load {input_}")
        case 404, *input_:
            print(f"bad load {input_}")
        case _:
            print(f"unknown command, {input_[0],input_[1].split()=}")


response([200, "http"])
response([404, "http error"])
response([906, "http error"])


@dataclass(frozen=False)
class Student:
    """Showing getattr setattr"""

    marks: int = 88
    name: str = "Sheeran"


person = Student()

# set value of name to Adam
setattr(person, "name", "Adam")
print(person.name)

# set value of marks to 78
setattr(person, "marks", 78)
print(person.marks)

# Output: Adam
#         78

person.name = "jill"

print(person)

print(getattr(person, "marks"))

print(f"""{hasattr(person, "__init__")=}""")

print(f"""{hasattr(person, "__repr__")=}""")

print(f"""{hasattr(person, "__str__")=}""")

print(f"""{hasattr(person, "__name__")=}""")


RANKS = "2,3,4,5,6,7,8,9,10,J,Q,K,A".split(",")
SUITS = "H,D,C,S".split(",")


@dataclass(order=True, frozen=True)
class Card:
    rank: str = field(compare=False)
    suit: str = field(compare=False)
    value: int = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, "value", RANKS.index(self.rank) + 1)
        print(RANKS, RANKS.index(self.rank))

    def __add__(self, other):
        if isinstance(other, Card):
            return self.value + other.value
        return self.value + other

    def __str__(self):
        return f"{self.rank} of {self.suit}"


my_card = Card("2", "S")
card2 = Card("3", "H")
print(my_card, card2)

print(my_card + card2)
