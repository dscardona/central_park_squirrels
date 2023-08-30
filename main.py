import pandas
# Read csv file
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# Get Primary Fur Color column data
color = data["Primary Fur Color"]
color_list = color.to_list()

# Find number of gray squirrels in column Primary Fur Color
# Find number of black squirrels in column Primary Fur Color
# Find number of cinnamon squirrels in column Primary Fur Color
# Create dictionary with extracted data
# Create dataframe from dictionary
# Create new CSV file