
# Export functions
import reports

def export(file_name):
    with open(file_name, "w") as f:
        f.write(str(reports.count_games("game_stat.txt")))
        f.write("\n")
        f.write(str(reports.decide("game_stat.txt", "1998")))
        f.write("\n")
        f.write(str(reports.get_latest("game_stat.txt")))
        f.write("\n")
        f.write(str(reports.count_by_genre("game_stat.txt", "RPG")))
        f.write("\n")
        f.write(str(reports.get_line_number_by_title("game_stat.txt", "World of Warcraft")))

export("answers.txt")
