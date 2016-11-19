import csv

# Additional function to open txt as csv
def open_as_csv(file_name):
    file = open(file_name, 'r')
    read_csv_file = csv.reader(file, delimiter='\t')
    csv_file = []
    for row in read_csv_file:
        csv_file.append(row)
    return csv_file

def count_games(file_name):
    numLines = 0
    file = open(file_name, 'r')
    for line in file:
        numLines+=1
    return numLines

def decide(file_name, year):
    file = open(file_name, 'r')
    lines = file.readlines()
    result = ''.join(lines)
    if str(year) in result:
        return True
    file.close()
    return False

def get_latest(file_name):
    csv_file = open_as_csv(file_name)
    latest_game = (sorted(csv_file, key=lambda x: x[2], reverse = True))
    return latest_game[0][0]

def count_by_genre(file_name, genre):
    csv_file = open_as_csv(file_name)
    genre_count=[]
    for i in range(len(csv_file)):
        if genre in csv_file[i]:
            genre_count.append(1)
    return(sum(genre_count))

def get_line_number_by_title(file_name, title):
    with open(file_name) as file:
        try:
            for num, line in enumerate(file, 1):
                if title in line:
                    return num
        except ValueError:
            return ValueError

def sort_abc(file_name):
    list =  open(file_name).readlines()
    sorted_list = []
    n = len(list) # Own algorithm for sorting starts here
    while n > 1:
        n-=1
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i] # Sorting algorithm ends here
    for line in list:
        sorted_list.append(line.split('\t', 1)[0])
    return sorted_list

def get_genres(file_name):
    csv_file = open_as_csv(file_name)
    genre_list = []
    for i in range(len(csv_file)):
        genre_list.append(csv_file[i][3])
    return (sorted(set(genre_list), key = str.lower))

def get_key(item):
    return float(item[1])

def when_was_top_sold_fps(file_name):
    csv_file = open_as_csv(file_name)
    fps_list = []
    try:
        for index in range(len(csv_file)):
            if 'First-person shooter' in csv_file[index]:
                fps_list.append(csv_file[index])
                most_sold_fps = (sorted(fps_list, key=get_key, reverse = True ))
        return int(most_sold_fps[0][2])
    except:
        return ValueError