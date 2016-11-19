import csv

# Additional function to open txt as csv
def open_as_csv(file_name):
    file = open(file_name, 'r')
    read_csv_file = csv.reader(file, delimiter='\t')
    csv_file = []
    for row in read_csv_file:
        csv_file.append(row)
    return csv_file

def get_most_played(file_name):
    csv_file = open_as_csv(file_name)
    csv_sorted = sorted(csv_file, key = lambda x: float(x[1]), reverse = True)
    return (csv_sorted[0][0])

def sum_sold(file_name):
    csv_file = open_as_csv(file_name)
    total_sold = []
    for index in range(len(csv_file)):
        total_sold.append(float(csv_file[index][1]))
    return sum(total_sold)

def get_selling_avg(file_name):
    csv_file = open_as_csv(file_name)
    total_sold = []
    for index in range(len(csv_file)):
        total_sold.append(float(csv_file[index][1]))
    return sum(total_sold) / len(total_sold)

def count_longest_title(file_name):
    csv_file = open_as_csv(file_name)
    titles = [csv_file[index][0] for index in range(len(csv_file))]
    titles_lengt = [len(element) for element in titles]
    return max(titles_lengt)

def get_date_avg(file_name):
    csv_file = open_as_csv(file_name)
    years_list = [int(csv_file[index][2]) for index in range(len(csv_file))]
    return round(sum(years_list) / len(years_list))

def get_game(file_name, title):
    csv_file = open_as_csv(file_name)
    for line in csv_file:
        if title == line[0]:
            line[1], line[2] = float(line[1]), float(line[2])
            return line

def count_grouped_by_genre(file_name):
    csv_file = open_as_csv(file_name)
    genre_dict_value = []
    for index in range(len(csv_file)):
        genre_dict_value.append(csv_file[index][3])
    genre_dict_value = sorted(genre_dict_value, key=str.lower)
    genre_dict_key = (sorted(set(genre_dict_value), key=str.lower))
    genre_dict_value_final = []
    for i in genre_dict_key:
        genre_dict_value_final.append(genre_dict_value.count(i))
    genre_count_dict = dict(zip(genre_dict_key, genre_dict_value_final))
    return genre_count_dict

def get_date_ordered(file_name):
    csv_file = open_as_csv(file_name)
    date_ordered = (sorted(csv_file, key=lambda x: x[2], reverse = True))
    n = len(date_ordered)
    while n > 1:
        n-=1
        for index in range(len(date_ordered)-1):
            if date_ordered[index][2] == date_ordered[index + 1][2] and date_ordered[index] > date_ordered[index + 1]:
                date_ordered[index], date_ordered[index + 1] = date_ordered[index +1], date_ordered[index]
    return [date_ordered[element][0] for element in range(len(date_ordered))]

