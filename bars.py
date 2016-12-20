import json
from math import sqrt

max_seats_count = 0
def load_data(filepath):
    with open(filepath) as f:
        lines = f.read()
        return json.loads(lines)



def get_biggest_bar(data):
    js = data
    global max_seats_count
    largest_bar = ''
    for i in js:
        if i['TypeObject'] == 'бар':
            if int(i['SeatsCount']) > max_seats_count:
                max_seats_count = i['SeatsCount']
                largest_bar = i['Name']
    return "Самый большой бар - {} , Число мест - {} ".format(largest_bar, max_seats_count )

def get_smallest_bar(data):
    js = data
    min_seats_count = max_seats_count
    smallest_bar = ''
    for i in js:
        if i['TypeObject'] == 'бар':
            if int(i['SeatsCount']) < max_seats_count:
                min_seats_count = i['SeatsCount']
                smallest_bar = i['Name']
    return "Самый маленький бар - {} , Число мест - {} ".format(smallest_bar, min_seats_count)



def get_closest_bar(data, longitude, latitude):
    js = data
    my_long = longitude
    my_latt = latitude
    min_dist = 1000
    nearest_bar = ''
    near_long = 0
    near_latt = 0
    near_add = ''
    for i in js:
        if i['TypeObject'] == 'бар':
            cur_long = float(i['geoData']['coordinates'][0])
            cur_latt = float(i['geoData']['coordinates'][1])
            cur_dist = sqrt((cur_long - my_long) ** 2 + (cur_latt - my_latt) ** 2)
            if cur_dist < min_dist:
                min_dist = cur_dist
                nearest_bar = i['Name']
                near_long = cur_long
                near_latt = cur_latt
                near_add = i['Address']
    return "Ближайший бар - {} , адрес - {} ".format(nearest_bar, near_add)



if __name__ == '__main__':
    filepath = input("Введите путь к файлу\n")
    data = load_data(filepath)
    print(get_biggest_bar(data))
    print(get_smallest_bar(data))
    longitude = float(input("Введите долготу в формате 37.62045190430437\n"))
    latitude = float(input("Введите широту в формате 55.768855394895915\n"))
    print(get_closest_bar(data, longitude, latitude))