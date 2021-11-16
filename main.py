# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd
import os
import sys

#defining filename
print("Enter input filename(include file extension): ", end='')
inputFilename = input()


#checking if it exists and exiting if it doesn't
if not os.path.exists(inputFilename):
    print("Cannot find input file "+inputFilename, file=sys.stderr)
    sys.exit(1)

#reading data
df = pd.read_csv(inputFilename)

#sorting both fields
df = df.sort_values(["division", "points"], ascending=(True, False))

#printing out the results as specified
print("records:")
for i in range(0,3):
    print("- name: "+ str(df["firstname"].iloc[i]) + " " + str(df["lastname"].iloc[i]))
    print("  details: In division "+ str(df["division"].iloc[i]) + " from " + str(df["date"].iloc[i]) + " performing " + str(df["summary"].iloc[i]))








