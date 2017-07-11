import reports


def exporting_answers():
    with open("export_answers.txt", "w") as f:
        f.write(str(reports.get_most_played("/home/daniel/codecool/3rd_si/pbwp-3rd-si-game-statistics-flachdaniel/part2/game_stat.txt")))
        f.write("\n")
        f.write(str(reports.sum_sold("/home/daniel/codecool/3rd_si/pbwp-3rd-si-game-statistics-flachdaniel/part2/game_stat.txt")))
        f.write("\n")
        f.write(str(reports.get_selling_avg("/home/daniel/codecool/3rd_si/pbwp-3rd-si-game-statistics-flachdaniel/part2/game_stat.txt")))
        f.write("\n")
        f.write(str(reports.count_longest_title(
            "/home/daniel/codecool/3rd_si/pbwp-3rd-si-game-statistics-flachdaniel/part2/game_stat.txt")))
        f.write("\n")
        f.write(str(reports.get_date_avg("/home/daniel/codecool/3rd_si/pbwp-3rd-si-game-statistics-flachdaniel/part2/game_stat.txt")))
        f.write("\n")
        f.write(str(reports.get_game(
            "/home/daniel/codecool/3rd_si/pbwp-3rd-si-game-statistics-flachdaniel/part2/game_stat.txt", "Minecraft")))


if __name__ == "__main__":
    exporting_answers()
