# loop through data folder and combine all the csvs together
# output: one csv file with all the data

import os
import pandas as pd

# get the current working directory
cwd = os.getcwd()

# get the data folder
data_folder = os.path.join(cwd, "data")

# get the list of files in the data folder
files = os.listdir(data_folder)

# create an empty list to store the data
data = []

# loop through the files
for file in files:
    # check if the file is a csv file
    if file.endswith(".csv"):
        # read the csv file
        df = pd.read_csv(os.path.join(data_folder, file))
        # append the data to the list
        data.append(df)
        print(f"Processed {file}")

# concatenate the data
df = pd.concat(data)

# save the data to a csv file
df.to_csv("nba_data.csv", index=False)
