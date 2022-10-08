

listyears = [1721,
979,
366,
299,
675,
1456,]

from numpy import genfromtxt
my_data = genfromtxt('day01.txt', delimiter=' ')

print(my_data)

listyears=list(my_data)
for year1 in listyears:
    for year2 in listyears:
        if year1+year2 == 2020:
            print(year1*year2)

#listyears=list(my_data)
for year1 in listyears:
    for year2 in listyears:
        for year3 in listyears:
            if year1+year2+year3 == 2020:
                print(year1*year2*year3)
