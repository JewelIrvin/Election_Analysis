# Assign a variable for the file to load and the path
import csv
import os

# Assign a variable to load a file from a path.

file_to_load = 'election_results.csv'

# Assign a variable to save the file to a path.

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file

with open(file_to_load) as election_data:

 # To do: read and analyze the data here.
    file_reader = csv.reader(election_data) 

# Print each row in the CSV file.
    headers = next(file_reader)
    print(headers)

#Close the file

