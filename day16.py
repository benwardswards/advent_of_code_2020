from dataclasses import dataclass, field
from rich import traceback, print
from parse import findall, parse
from pathlib import Path

traceback.install()

DATA_STR = Path("day16.txt").read_text()

TEST_STR = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""


@dataclass
class validTickets:
    valid_set: set[int]
    valids: list[dict[str, int]]
    your_tickets: list[int]
    nearby_tickets: list[list[int]]
    nearby_valid: list[list[int]]

    def __init__(self, input_str: str):
        self.valids = []
        ranges, your_tickets, nearby_tickets = input_str.split("\n\n")
        for item in ranges.splitlines():
            self.valids.append(
                parse("{name}: {start1}-{end1} or {start2}-{end2}", item).named
            )

        self.your_tickets = [
            int(num) for num in your_tickets.splitlines()[1].split(",")
        ]

        self.nearby_tickets = []
        print(nearby_tickets.splitlines())
        for ticket in nearby_tickets.splitlines()[1:]:
            self.nearby_tickets.append([int(num) for num in ticket.split(",")])

        self.valid_set = set()
        self.nearby_valid = list()

    def get_valid_set(self):
        for vals in self.valids:
            self.valid_set |= set(range(int(vals["start1"]), int(vals["end1"]) + 1))
            self.valid_set |= set(range(int(vals["start2"]), int(vals["end2"]) + 1))

    def sum_invalids_any(self):
        total = 0

        for line in self.nearby_tickets:
            good_ticket = True
            for ticket in line:
                if ticket not in self.valid_set:
                    good_ticket = False
                    total += ticket
                    break
            if good_ticket:
                self.nearby_valid.append(line)

        return total

    def find_fields(self):

        tickets_spec = [set() for _ in range(len(self.nearby_valid[0]))]
        for line in self.nearby_valid:
            for i, num in enumerate(line):
                tickets_spec[i].add(num)
        print("ticket groups", tickets_spec)

        ticket_fields = dict()

        first_set = tickets_spec[0]
        for line in self.valids:
            ticket_fields[line["name"]] = []
            for igroup, ticket_group in enumerate(tickets_spec):
                is_good = True
                for num in ticket_group:
                    cond1 = int(line["start1"]) <= num <= int(line["end1"])
                    cond2 = int(line["start2"]) <= num <= int(line["end2"])

                    if not (cond1 or cond2):
                        is_good = False
                        break
                if is_good == True:
                    ticket_fields[line["name"]].append(igroup)

        print(f"{ticket_fields=}")

        done = []
        n_fields = len(self.valids)
        while len(done) < n_fields:
            for key, value_list in ticket_fields.items():
                if len(value_list) == 1 and key not in done:
                    print(f"poping {key}")
                    # pop keys off outher lists
                    for superkey in ticket_fields.keys():
                        if (
                            superkey not in done
                            and superkey != key
                            and value_list[0] in ticket_fields[superkey]
                        ):
                            ticket_fields[superkey].remove(value_list[0])
                    done.append(key)
                    break
        print(done, ticket_fields)

        out_total = 1
        for key, value in ticket_fields.items():
            if key.startswith("dep"):
                print(key, value, self.your_tickets[value[0]])
                out_total *= self.your_tickets[value[0]]
        print("departures_total of your ticket ", out_total)
        return out_total


test_ticket = validTickets(TEST_STR)
print(test_ticket)
test_ticket.get_valid_set()
# print(test_ticket.valid_set)S

print(test_ticket.sum_invalids_any())
print("nearby valid:", test_ticket.nearby_valid)
test_ticket.find_fields()

###############################
test_ticket = validTickets(DATA_STR)
# print(test_ticket)
test_ticket.get_valid_set()

# print(test_ticket.valid_set)
#
print(test_ticket.sum_invalids_any())
test_ticket.find_fields()


# print("number of valid tickets nearby", len(test_ticket.nearby_valid))
# print("number of nearby tickets nearby", len(test_ticket.nearby_tickets))
