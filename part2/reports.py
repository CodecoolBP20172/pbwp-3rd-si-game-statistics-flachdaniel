import math


def to_list(file_name):
    table = []
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        table = [element.replace("\n", "").split("\t") for element in lines]
        for i in range(len(table)):
            table[i][1] = float(table[i][1])
            table[i][2] = int(table[i][2])
    except FileNotFoundError:
        return "Invalid file name"
    return table


def get_most_played(file_name):
    table = to_list(file_name)
    max_sold = 0
    name = ""
    for i in range (len(table)):
        if table[i][1] > float(max_sold):
            max_sold = table[i][1]
            name = table[i][0]
    return name


def sum_sold(file_name):
    table = to_list(file_name)
    sum_sold = 0
    for i in range (len(table)):
        sum_sold += table[i][1]
    return sum_sold


def get_selling_avg(file_name):
    copies = sum_sold(file_name)
    table = to_list(file_name)
    return copies/len(table)


def get_game(file_name, title):
    table = to_list(file_name)
    for i in range (len(table)):
        if title == table[i][0]:
            return table[i]
    return "There is no game with that title"


def get_date_avg(file_name):
    table = to_list(file_name)
    average_year = 0
    for i in range (len(table)):
        average_year += table[i][2]
    return math.ceil(average_year/len(table))


def count_longest_title(file_name):
    table = to_list(file_name)
    longest_title = 0
    for i in range (len(table)):
        if longest_title < len(table[i][0]):
            longest_title = len(table[i][0])
    return longest_title



print (count_longest_title("/home/daniel/codecool/3rd_si/pbwp-3rd-si-game-statistics-flachdaniel/part2/game_stat.txt"))