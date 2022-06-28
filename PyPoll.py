# The data we need to retrieve.
# 1. The tota lnumber of votes cast
# 2 A complete list of candidates who received votes
# 3 The percentage of votes each candidate won
# 4 The total number of votes each candidate won
# 5 The winner of the election based on populaar vote.


import csv

# Assign a variable to load a file from a path.
file_to_load =  'C:\\Users\\lawof\\Desktop\\Bootcamp\\3\\election_results.csv'

# Assign a variable for the file to load and the path.
file_to_save = 'C:\\Users\\lawof\\Desktop\\Bootcamp\\3\\election_analysis\\analysis\\election_analysis.txt'

with open(file_to_load, "r") as election_data:

 # To do: perform analysis.
    file_reader =  csv.reader(election_data)

# Read and print the header row.
    headers = next(file_reader)
    print(headers)

    for row in file_reader:
        print(row)
        
# Close the file.
election_data.close()