# Import modules
import os 
import csv

# Path for file
csvpath = os.path.join('python_challenge', 'PyBank', 'Resources', 'budget_data.csv')

# Path to analysis text file
analysispath = os.path.join('python_challenge', 'PyBank', 'analysis', 'Analysis.txt')

# Reading csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)

# Create variables 
total_months = 0

total_profit = 0

avg_change = 0

max_increase = 0
increase_index = 0

max_decrease = 0
decrease_index = 0

# Create lists
profit_loss = []

profit_change = [0]

dates = []

# Financial Analysis for loops
for row in csvreader:
    total_months += 1
    profit_loss.append(int(row[1]))
    dates.append(str(row[0]))

for i in range(0, total_months - 1):
    profit_change.append((profit_loss[i+1])-(profit_loss[i]))

for j in range(0,total_months):
    if (profit_change[j] > max_increase):
        max_increase = profit_change[j]
        increase_index = j

for k in range(0,total_months):
    if (profit_change[k] > max_decrease):
        max_decrease = profit_change[k]
        decrease_index = k

# Print analysis
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")

total_profit = sum(profit_loss)
print(f"Total: ${total_profit}")

avg_change = sum(profit_change)/(total_months - 1)
print(f"Average Change: ${round(avg_change,2)}")

print(f"Greatest Increase in Profits: {dates[increase_index]} ${max_increase}")
print(f"Greatest Decrease in Profits: {dates[decrease_index]} ${max_decrease}")




