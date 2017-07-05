
# Report functions
def count_games(file_name):
    count = 0
    try:
        with open(file_name) as file:
            for line in file:
                count += 1
        return count
    except FileNotFoundError:
        return "Invalid file name"

def decide(file_name,year):
    year = str(year)
    try:
        with open(file_name) as file:
            for line in file:
                if year in line:
                    return True
        return False
    except FileNotFoundError:
        return "Invalid file name"

def get_latest(file_name):
    list_of_lines = []
    years_and_names = {}
    try:
        with open(file_name) as file:
            for line in file:
                list_of_lines.append(line.split("\t"))
            for i in range(len(list_of_lines)):
                years_and_names.update({list_of_lines[i][0]:list_of_lines[i][2]})
        return max(years_and_names, key=years_and_names.get)
    except FileNotFoundError:
        return "Invalid file name"

def count_by_genre(file_name, genre):
    genre = str(genre)
    count = 0
    list_of_lines = []
    genres = []
    try:
        with open(file_name) as file:
            for line in file:
                list_of_lines.append(line.split("\t"))
            for i in range(len(list_of_lines)):
                if genre == list_of_lines[i][3]:
                    count += 1
            if count > 0:
                return count
            else:
                return "There is no game with that genre"
    except FileNotFoundError:
        return "Invalid file name"

def get_line_number_by_title(file_name, title):
    count = 1
    list_of_lines = []
    try:
        with open(file_name) as file:
            for line in file:
                list_of_lines.append(line.split("\t"))
            for i in range(len(list_of_lines)):
                if title == list_of_lines[i][0]:
                    return count
                else:
                    count += 1
        raise ValueError
    except ValueError:
        return "There is no game with that title"
    except FileNotFoundError:
        return "Invalid file name"



print(count_games("/home/daniel/codecool/3rd_si/pbwp-3rd-si-game-statistics-flachdaniel/game_stat.txt"))
