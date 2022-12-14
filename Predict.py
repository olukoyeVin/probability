from tabulate import tabulate
from os import name as SystemName, system

# attend = [
#     ["1","rainy","yes"],
#     ["2","sunny","no"],
#     ["3","cloudy","yes"],
#     ["4","cloudy","no"],
#     ["5","sunny","no"],
#     ["6","rainy","yes"],
#     ["7","sunny","yes"],
#     ["8","cloudy","no"],
#     ["9","rainy","no"],
#     ["10","sunny","no"],
#     ["11","sunny","yes"],
#     ["12","rainy","no"],
#     ["13","cloudy","yes"],
#     ["14","cloudy","yes"],
# ]
# attend = [
#     ["1", "rainy", "yes"],
#     ["2", "sunny", "yes"],
#     ["3", "cloudy", "yes"],
#     ["4", "cloudy", "yes"],
#     ["5", "sunny", "no"],
#     ["6", "rainy", "yes"],
#     ["7", "sunny", "yes"],
#     ["8", "cloudy", "yes"],
#     ["9", "rainy", "no"],
#     ["10", "sunny", "no"],
#     ["11", "sunny", "yes"],
#     ["12", "rainy", "no"],
#     ["13", "cloudy", "yes"],
#     ["14", "cloudy", "yes"],
# ]

attend = [[]]
print("How many days to include in calculation")
num_days = eval(input())

for x in range(num_days):
    if (len(attend) == 1) and not len(attend[0]):
        attend[0] = [x + 1]
    else:
        attend.append([x + 1])

weather = {
    "s": "sunny",
    "r": "rainy",
    "c": "cloudy"
}
attendance = {
    "y": "yes",
    "n": "no"
}


def clearScreen():
    if SystemName == "nt":
        _ = system('cls')
    else:
        _ = system('clear')


for row in attend:
    clearScreen()
    print("Reply with (c,s,r) for weather:\n\ts = Sunny\n\tc = Cloudy\n\tr = Rainy")
    print("DAY {} DATA".format(row[0]))
    print("What was the weather?")
    row.append(weather[input()])
    print("What was the attendance? (y/n)")
    row.append(attendance[input()[0]])

table1 = [["weather", "yes", "no", "probability", "outcome"]]

for day in attend:
    x = 0
    for row in table1:
        if len(row) > 0:
            if (day[1] != row[0]) and (x == len(table1) - 1):
                table1.append([day[1], 0, 0, 0.0, ""])
            elif day[1] == row[0]:
                continue
        x += 1

table1.append(["", 0.0, 0.0, ""])

for row in table1:
    for row2 in attend:
        if (row[0] == row2[1]) and (row2[2] == "yes"):
            row[1] += 1
        elif (row[0] == row2[1]) and (row2[2] == "no"):
            row[2] += 1

count_yes = 0
count_no = 0
count_row = 0
for row in table1:
    if count_row >= 1:
        if count_row < len(table1) - 1:
            row[3] = "%.3f" % ((row[1] + row[2]) / len(attend))
        count_yes += row[1]
        count_no += row[2]
    count_row += 1

table1[len(table1) - 1][1] = "%.3f" % (count_yes / (count_yes + count_no))
table1[len(table1) - 1][2] = "%.3f" % (count_no / (count_yes + count_no))

prob_y = table1[len(table1) - 1][1]
prob_n = table1[len(table1) - 1][2]


def get_prob(x, y, z):
    x = float(x)
    y = float(y)
    z = float(z)
    return (x * y) / z


def get_outcome(y, n, z):
    positive = get_prob(y, prob_y, z)
    negative = get_prob(n, prob_n, z)

    if positive > negative:
        return "will attend"
    elif positive < negative:
        return "will not attend"
    elif positive == negative:
        return "unknown"


count_row = 0
for row in table1:
    if 0 < count_row < len(table1) - 1:
        row[len(table1) - 1] = get_outcome((row[1] / count_yes), (row[2] / count_no), row[3])

    count_row += 1

table1_copy = table1[:]
table1_copy.pop(0)
print(tabulate(tabular_data=table1_copy, headers=table1[0], tablefmt='org tbl'))
