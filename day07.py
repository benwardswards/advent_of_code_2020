from rich import print

# from dataclasses import dataclass

with open("day7.txt") as file:
    data = file.read()

testdata = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

testdata2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

print(testdata)


def prepare_data(data_in: str) -> list[list[str]]:
    testdata = (
        data_in.replace(".", "")
        .replace(",", "")
        .replace("bags", "bag")
        .replace("contain", "")
    )

    testprep = [line.split("bag")[:-1] for line in testdata.splitlines()]
    return [[item.strip() for item in line] for line in testprep]


test_data_prepared = prepare_data(testdata)
data_prepared = prepare_data(data)
test_data_prepared2 = prepare_data(testdata2)


print(test_data_prepared)
print(data_prepared[:3])


def colors_contain(start_bag: str, bag_rules: list[list[str]]) -> int:
    contain_gold: set[str] = set([start_bag])
    contain_gold_old: set[str] = set()
    while contain_gold != contain_gold_old:
        contain_gold_old = contain_gold.copy()
        for bag in bag_rules:
            for inner_bag in bag[1:]:
                if inner_bag == "no other":
                    pass
                else:
                    name = " ".join(inner_bag.split()[1:])
                    if name in contain_gold:
                        contain_gold.add(bag[0])
    # print(contain_gold)
    return len(contain_gold) - 1


assert colors_contain("shiny gold", test_data_prepared) == 4
print(f"""{colors_contain('shiny gold', data_prepared)=}""")


def howmanybags(start_bag: str, data: list[list[str]]) -> int:
    bag_dict: dict[str, list[str]] = {bag: inner for bag, *inner in data}

    def howmany(start_bag: str) -> int:
        inner_bags = bag_dict[start_bag]
        if inner_bags == ["no other"]:
            return 0

        total = 0
        for bag in inner_bags:
            number, *bag_name = bag.split()
            bag_name_j = " ".join(bag_name)
            total += int(number) * (1 + howmany(bag_name_j))

        return total

    return howmany(start_bag)


assert howmanybags("vibrant plum", test_data_prepared) == 11
assert howmanybags("shiny gold", test_data_prepared) == 32
assert howmanybags("faded blue", test_data_prepared) == 0
assert howmanybags("shiny gold", test_data_prepared2) == 126


print("shiny gold", howmanybags("shiny gold", data_prepared), "bags")
