# Import modules
import os 
import csv

# Path for file
csvpath = os.path.join('python_challenge', 'PyPoll', 'Resources', 'election_data.csv')

# Reading csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)