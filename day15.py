from dataclasses import dataclass, field
from rich import traceback, print
from collections import defaultdict

traceback.install()

TEST1 = [0, 3, 6]


@dataclass
class Memory:
    last: int
    game_start: list[int]
    last_played: dict[int, int] = field()

    def __init__(self, game_list):
        self.game_start = game_list
        self.last_played = dict()
        for turn, number in enumerate(game_list):
            self.last_played[number] = turn
        self.last = 0  # instiallizing the game

    def run(self, total: int):
        for turn in range(len(self.game_start) + 1, total):
            last_position = self.last_played.get(self.last)
            if last_position is None:
                age = 0
            else:
                age = turn - last_position - 1

            self.last_played[self.last] = turn - 1
            self.last = age
            # print(self.last)
        return self.last


memory = Memory(TEST1)
print(memory)

assert memory.run(10) == 0, memory.run(10)
print([0, 3, 6, 0, 3, 3, 1, 0, 4, 0])

assert Memory([1, 3, 2]).run(2020) == 1, Memory([1, 3, 2]).run(2020)
assert Memory([2, 1, 3]).run(2020) == 10
assert Memory([3, 2, 1]).run(2020) == 438
assert Memory([3, 1, 2]).run(2020) == 1836

print(Memory([0, 13, 1, 8, 6, 15]).run(2020))

# Memory([0, 3, 6]).run(30_000_000)

# assert Memory([0, 3, 6]).run(30_000_000) == 175594

print("part_B", Memory([0, 13, 1, 8, 6, 15]).run(30_000_000))
