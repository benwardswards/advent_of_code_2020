test_str = """939
7,13,x,x,59,x,31,19"""

with open("day13.txt") as file:
    data_str = file.read()

start_time = 939


def next_time(time: int, frequency: int) -> int:
    return time - time % frequency + frequency


assert next_time(start_time, 7) == 945, next_time(start_time, 7)
assert next_time(start_time, 13) == 949
assert next_time(start_time, 59) == 944


def wait_time(test_str: str) -> int:
    time, commands = test_str.splitlines()
    time = int(time)
    command_list = commands.split(",")

    # print(start_time, command_list)

    times = {}
    for bus in command_list:
        if bus == "x":
            pass
        else:
            times[int(bus)] = next_time(time, int(bus))

    min_bus, min_time = min(times.items(), key=lambda x: x[1])
    return min_bus * (min_time - time)


print(f" the min time * min_id = {wait_time(test_str)}")
print(f" the min time * min_id = {wait_time(data_str)}")


def wait_time_b(commands: str) -> int:
    "implemnts the chinese remainder theorm. all buses must be relativel prime and non repeated."
    command_list: list[list[int]] = []
    for ibus, bus in enumerate(commands.split(",")):
        if bus != "x":
            command_list.append([ibus, int(bus)])

    # chinesse remainder theorm is faster if you start with biggest values
    command_list.sort(key=(lambda d: d[1]), reverse=True)

    jump = command_list[0][1]
    time = (jump - command_list[0][0]) % jump
    print(f"To start {jump=}{time=}")
    print(command_list)
    for remainder_bus, bus in command_list[1:]:
        while True:
            time += jump
            print(f"{time=}{remainder_bus=},{bus=}{jump=} ")
            if time % bus == (bus - remainder_bus) % bus:
                jump *= bus
                break
    return time


print(wait_time_b("17,x,13,19"), "should be 3417")

print(wait_time_b("67,7,59,61"), "should be 754018")
print(wait_time_b("1789,37,47,1889"), "should be 1202161486")
print(wait_time_b(data_str.splitlines()[1]), "should be 1202161486")
