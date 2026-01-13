import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# temp_avg = sum(temp_list) / len(temp_list)
# print(temp_avg)
# print(data["temp"].mean())#average
#
# print(data["temp"].max())

#get data in columns
# print(data["condition"])
# print(data.condition)

#get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32

#create a dataframe from scratch
data_dict = {
    "students": ["Amy", "Viv", "Angel"],
    "scores": [76, 99, 94]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")