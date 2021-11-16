# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd
import os
import sys

#defining filename
print("Enter input filename(include file extension): ")
filename = input()

#checking if it exists and exiting if it doesn't
if not os.path.exists(filename):
    print("Cannot find input file "+filename, file=sys.stderr)
    sys.exit(1)

#reading data
df = pd.read_csv(filename)

#sorting both fields
df = df.sort_values(["division", "points"], ascending=(True, True))




print(df)


