# Import modules
import os 
import csv

# Path for file
csvpath = os.path.join('python_challenge', 'PyPoll', 'Resources', 'election_data.csv')

# Path to analysis text file
analysispath = os.path.join('python_challenge', 'PyPoll', 'analysis', 'Analysis.txt')

# Reading csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)

    poll = list(csvreader)

# Election analysis
total_votes = len(poll)

candidates = set()

vote_count = 0

for row in poll:
    if row[2] not in candidates:
        candidates.add(row[2])

max_votes = 0
winner = ''

for candidate in candidates:
    for row in poll:
        if candidate == row[2]:
            vote_count += 1
        if vote_count > max_votes:
            max_votes = vote_count
            winner = candidate

vote_percent = round(vote_count / total_votes * 100, 3)

# Print analysis
print(f"Election Results")
print(f"----------------")
print(f"Total Votes: {total_votes}")
print(f"--------------------------")
print(f"{candidate}: {vote_percent}% {(vote_count)}")
print(f"-------------------------------------------")
print(f"Winner: {winner}")
print(f"----------------")
