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

    def __repr__(self):
        return f"{self.accumlator=},{self.location=}"

    def process_intruction(self):
        next_instr = self.instructions[self.location]
        print(f"{self}", next_instr, end=" ")
        if next_instr.name == "nop":
            self.location += 1
        elif next_instr.name == "jmp":
            self.location += next_instr.value
        elif next_instr.name == "acc":
            self.accumlator += next_instr.value
            self.location += 1
        else:
            raise TypeError("Invalid instruction")

    def run_terminated(self):
        while self.location not in self.visited:
            self.visited.append(self.location)
            self.process_intruction()
            if self.location >= self.max_loc:
                print("program terminated")
                print(self)
                return True

        print(f"visted {self.location} again, done!{self.accumlator=}")
        return False


def find_wrong_instruction(program: list[str]):
    for i, instruction in enumerate(program):
        current_ins = Instr(instruction)
        if current_ins.name == "nop":
            testprogram1 = program.copy()
            testprogram1[i] = "jmp" + " " + str(current_ins.value)
            if Console(testprogram1).run_terminated():
                print(i, instruction, "nop->jmp")
                break
        elif current_ins.name == "jmp":
            testprogram1 = program.copy()
            testprogram1[i] = "nop" + " " + str(current_ins.value)
            if Console(testprogram1).run_terminated():
                print(i, instruction, "jmp->nop")
                break


test_console = Console(testprogram)
print(test_console)
test_console.run_terminated()

console = Console(program)
console.run_terminated()

find_wrong_instruction(testprogram)

find_wrong_instruction(program)
