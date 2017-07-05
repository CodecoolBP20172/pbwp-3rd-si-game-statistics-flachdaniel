
# Report functions
def count_games(file_name):
    count = 0
    with open(file_name) as file:
        for line in file:
            count += 1
    return count

def decide(file_name,year):
    year = str(year)
    with open(file_name) as file:
        for line in file:
            if year in line:
                return True
        return False

def get_latest(file_name):
    list_of_lines = []
    years_and_names = {}
    with open(file_name) as file:
        for line in file:
            list_of_lines.append(line.split("\t"))
        for i in range(len(list_of_lines)):
            years_and_names.update({list_of_lines[i][0]:list_of_lines[i][2]})
        return max(years_and_names, key=years_and_names.get)




print(get_latest("/home/daniel/codecool/3rd_si/pbwp-3rd-si-game-statistics-flachdaniel/game_stat.txt"))
