import pandas

squirrel_data = pandas.read_csv(
    "D:/Python/python/Day-25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231031.csv")

count_grey = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
count_cinnamon = len(
    squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
count_black = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])


data_dict = {"Fur Color": ["grey", "red", "black"],
             "Count": [count_grey, count_cinnamon, count_black]}

data = pandas.DataFrame(data_dict)
data.to_csv("D:/Python/python/Day-25/new_csv.csv")
