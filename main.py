import pandas

# Read csv file
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# # Get Primary Fur Color column data
# color = data["Primary Fur Color"]
# color_list = color.to_list()

# # Find number of gray, black, cinnamon squirrels in column Primary Fur Color
# gray = color_list.count("Gray")
# black = color_list.count("Black")
# cinnamon = color_list.count("Cinnamon")

# # Create dictionary with extracted data
# color_dict = {
#     "fur color" : ["gray", "black", "cinnamon"],
#     "count" : [gray, black, cinnamon]
# }

# # Create dataframe from dictionary
# new_data = pandas.DataFrame(color_dict)

# # Create new CSV file
# new_data.to_csv("squirrel_colors.csv")


## ALTERNATIVE SOLUTION

# Extract data
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

# Create Dictionary
data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

print(data_dict)

#Create dataframe and csv file as seen above