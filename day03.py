with open("day03.txt") as file:
    data = file.read().splitlines()

print(data)


#   Right 1, down 1.
#   Right 3, down 1. (This is the slope you already checked.)
#   Right 5, down 1.
#   Right 7, down 1.
#   Right 1, down 2.


def numberoftrees(data, right, down):
    number_of_trees = 0
    data_len = len(data[0])
    for i, line in enumerate(data):
        print(i % down)
        if line[(i * right // down) % data_len] == "#" and i % down == 0:
            number_of_trees += 1
    return number_of_trees


total = (
    numberoftrees(data, 1, 1)
    * numberoftrees(data, 3, 1)
    * numberoftrees(data, 5, 1)
    * numberoftrees(data, 7, 1)
    * numberoftrees(data, 1, 2)
)
# print(numberoftrees(data,7,1))
# print(numberoftrees(data,1,2))
print(total)
