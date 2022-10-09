from dis import Instruction
from logging import exception
from sre_constants import MAX_UNTIL
from rich import print

from dataclasses import dataclass

with open("day8.txt") as file:
    program = file.read().splitlines()

print(program)


testprogram = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".splitlines()

print(testprogram)


@dataclass
class Instr:
    name: str
    value: int

    def __init__(self, str_instruction: str):
        first, second = str_instruction.split(" ")
        self.name = first
        self.value = int(second)


my_instr = Instr("jmp -4")

print(my_instr)


@dataclass
class Console:
    visited: list[int]
    instructions: list[Instr]
    accumlator: int = 0
    location: int = 0
    max_loc = 0

    def __init__(self, input_instructions: list[str]):
        self.instructions = [Instr(ins) for ins in input_instructions]
        self.max_loc = len(self.instructions)
        self.visited = list()

    def process_intruction(self):
        next_instr = self.instructions[self.location]
        print(f"{self.location=}", next_instr, end=" ")
        if next_instr.name == "nop":
            self.location += 1
        elif next_instr.name == "jmp":
            self.location += next_instr.value
        elif next_instr.name == "acc":
            self.accumlator += next_instr.value
            self.location += 1
        else:
            raise TypeError("Invalid instruction")

        if self.location >= self.max_loc:
            raise exception("invalid location")
        print(f"{self.accumlator=}")

    def run(self):
        while self.location not in self.visited:
            self.visited.append(self.location)
            self.process_intruction()

        print(f"visted {self.location} again, done!{self.accumlator=}")


test_console = Console(testprogram)
print(test_console)
test_console.run()

console = Console(program)
console.run()
