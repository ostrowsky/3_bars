import json
from math import sqrt

max_seats_count = 0
def load_data(filepath):
    with open(filepath) as input_file:
        file_content = input_file.read()
        return json.loads(file_content)


def get_biggest_bar(json_file):
    json_content = json_file
    global max_seats_count
    biggest_bar = ''
    for place in json_content:
        if place['TypeObject'] == 'бар':
            if int(place['SeatsCount']) > max_seats_count:
                max_seats_count = place['SeatsCount']
                biggest_bar = place['Name']
    return "Самый большой бар - {} , Число мест - {} ".format(biggest_bar, max_seats_count )


def get_smallest_bar(json_file):
    json_content = json_file
    min_seats_count = max_seats_count
    smallest_bar = ''
    for place in json_content:
        if place['TypeObject'] == 'бар':
            if int(place['SeatsCount']) < max_seats_count:
                min_seats_count = place['SeatsCount']
                smallest_bar = place['Name']
    return "Самый маленький бар - {} , Число мест - {} ".format(smallest_bar, min_seats_count)


def get_closest_bar(json_file, longitude, latitude):
    json_content = json_file
    my_long = longitude
    my_latt = latitude
    min_dist = 1000
    nearest_bar = ''
    near_long = 0
    near_latt = 0
    near_address = ''
    for place in json_content:
        if place['TypeObject'] == 'бар':
            cur_long = float(place['geoData']['coordinates'][0])
            cur_latt = float(place['geoData']['coordinates'][1])
            cur_dist = sqrt((cur_long - my_long) ** 2 + (cur_latt - my_latt) ** 2)
            if cur_dist < min_dist:
                min_dist = cur_dist
                nearest_bar = place['Name']
                near_long = cur_long
                near_latt = cur_latt
                near_address = place['Address']
    return "Ближайший бар - {} , адрес - {} ".format(nearest_bar, near_address)


if __name__ == '__main__':
    filepath = input("Введите путь к файлу\n")
    json_file = load_data(filepath)
    print(get_biggest_bar(json_file))
    print(get_smallest_bar(json_file))
    longitude = float(input("Введите долготу в формате 37.62045190430437\n"))
    latitude = float(input("Введите широту в формате 55.768855394895915\n"))
    print(get_closest_bar(json_file, longitude, latitude))