
# Report functions
def to_list(file_name):
    table = []
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        table = [element.replace("\n", "").split("\t") for element in lines]
    except FileNotFoundError:
        return "Invalid file name"
    return table


def get_most_played(file_name):
    table = to_list(file_name)
    max_sold = 0
    name = ""
    for i in range (len(table)):
        if float(table[i][1]) > float(max_sold):
            max_sold = table[i][1]
            name = table[i][0]
    return name

def sum_sold(file_name):
    table = to_list(file_name)
    sum_sold = 0
    for i in range (len(table)):
        sum_sold += float(table[i][1])
    return sum_sold

def get_selling_avg(file_name):
    copies = sum_sold(file_name)
    table = to_list(file_name)
    return copies/len(table)


print (get_selling_avg("/home/daniel/codecool/3rd_si/pbwp-3rd-si-game-statistics-flachdaniel/part2/game_stat.txt"))