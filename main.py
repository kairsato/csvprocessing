# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd

#reading in input
filename = "input.csv"
df = pd.read_csv(filename)

#sorting both fields
df = df.sort_values(["division", "points"], ascending=(True, True))

print(df)


