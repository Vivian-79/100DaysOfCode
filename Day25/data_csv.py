import csv

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import data_csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for raw in data:
        if raw[1] != "temp":
            temperatures.append(raw[1])
    print(temperatures)