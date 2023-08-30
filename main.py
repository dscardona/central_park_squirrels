import pandas

# Read csv file
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Get Primary Fur Color column data
color = data["Primary Fur Color"]
color_list = color.to_list()

# Find number of gray, black, cinnamon squirrels in column Primary Fur Color
gray = color_list.count("Gray")
black = color_list.count("Black")
cinnamon = color_list.count("Cinnamon")

# Create dictionary with extracted data
color_dict = {
    "fur color" : ["gray", "black", "cinnamon"],
    "count" : [gray, black, cinnamon]
}

# Create dataframe from dictionary
# new_data = pandas.DataFrame(color_dict)

# Create new CSV file
# new_data.to_csv("squirrel_colors.csv")