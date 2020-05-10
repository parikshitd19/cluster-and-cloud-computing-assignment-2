import sys, os, glob
import pandas as pd
import numpy as np
import data_constants

# loops through all of the aurin data and aggregates it into one dataframe
def aggregate_aurin_data():
    data = pd.DataFrame()
    for file_name in data_constants.melb_file_names:
        year_data = open_file(file_name)
        if data.empty:
            data = data.append(year_data)
        else:
            data = data.add(year_data)
    return data

# opens the given Aurin data file and reads the contents into a dataframe
def open_file(file_name):
    working_dir = os.getcwd()
    file_location = glob.glob(working_dir + "/**/" + file_name, recursive = True)
    data = pd.read_csv(file_location[0], sep = ',')
    data = data.set_index('postcode')
    return data

# Main method
if __name__ == "__main__":
    aggregated_data = aggregate_aurin_data()
    print(aggregated_data.head())
