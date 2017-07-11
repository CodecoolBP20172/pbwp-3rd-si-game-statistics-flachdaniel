import reports


def printing_reports():
    print(reports.get_most_played("/home/daniel/codecool/3rd_si/pbwp-3rd-si-game-statistics-flachdaniel/part2/game_stat.txt"))
    print(reports.sum_sold("/home/daniel/codecool/3rd_si/pbwp-3rd-si-game-statistics-flachdaniel/part2/game_stat.txt"))
    print(reports.get_selling_avg("/home/daniel/codecool/3rd_si/pbwp-3rd-si-game-statistics-flachdaniel/part2/game_stat.txt"))
    print(reports.count_longest_title("/home/daniel/codecool/3rd_si/pbwp-3rd-si-game-statistics-flachdaniel/part2/game_stat.txt"))
    print(reports.get_date_avg("/home/daniel/codecool/3rd_si/pbwp-3rd-si-game-statistics-flachdaniel/part2/game_stat.txt"))
    print(reports.get_game("/home/daniel/codecool/3rd_si/pbwp-3rd-si-game-statistics-flachdaniel/part2/game_stat.txt", "Minecraft"))
    print(reports.count_grouped_by_genre("/home/daniel/codecool/3rd_si/pbwp-3rd-si-game-statistics-flachdaniel/part2/game_stat.txt"))
    print(reports.get_date_ordered("/home/daniel/codecool/3rd_si/pbwp-3rd-si-game-statistics-flachdaniel/part2/game_stat.txt"))


if __name__ == "__main__":
    printing_reports()
