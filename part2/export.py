import reports
from reports import open_as_csv
from reports import get_most_played
from reports import sum_sold
from reports import get_selling_avg
from reports import count_longest_title
from reports import get_date_avg
from reports import get_game
from reports import count_grouped_by_genre
from reports import get_date_ordered

def export_results(question, value):
    export_file = open("reports.txt", "a")
    export_file.write(question + '\n' + str(value)+'\n')
    export_file.close()

export_results("What is the most played game", get_most_played("game_stat.txt"))
export_results("How many copies have been sold total (million)?", sum_sold("game_stat.txt"))
export_results("What is the average selling?", get_selling_avg("game_stat.txt"))
export_results("How many characters long is the longest title?", count_longest_title("game_stat.txt"))
export_results("What is the average of the release dates?", get_date_avg("game_stat.txt"))
export_results("What properties has a game?", get_game("game_stat.txt", "Diablo III"))
export_results("How many games are there grouped by genre?", count_grouped_by_genre("game_stat.txt"))
export_results("What is the date ordered list of the games? ", get_date_ordered("game_stat.txt"))