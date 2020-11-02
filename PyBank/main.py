import os
import csv

# path to csv file
csv_path = os.path.join("Resources", "budget_data.csv")

# declare variable to store data
total_months = []
total_profit = []
total_changes = []
average_changes = 0

# get data from file and put it to lists
with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_reader)

    for row in csv_reader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))

# calculate profit for each month (February - January; March - February and e.c.):
for i in range(len(total_profit) - 1):
    total_changes.append(total_profit[i+1] - total_profit[i])

# calculate average changes
average_changes = sum(total_changes) / len(total_changes)
# find greatest increase and decrease
greatest_increase = max(total_changes)
greatest_decrease = min(total_changes)
# find months for greatest increase and decrease. Add 1 to month because we commute profit between two months.
greatest_increase_month = total_months[total_changes.index(greatest_increase) + 1]
greatest_decrease_month = total_months[total_changes.index(greatest_decrease) + 1]

# print results to terminal
print("Financial Analysis")
print("---------------------------------")
print(f'Total months: {len(total_months)}')
print(f'Total: ${sum(total_profit)}')
print(f'Average change: ${round(average_changes, 2)}')
print(f'Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase}')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease}')

# write results to a file
with open('Analysis/report.csv', 'w') as writer:
    writer.write("Financial Analysis\n")
    writer.write("---------------------------------\n")
    writer.write(f'Total months: {len(total_months)}\n')
    writer.write(f'Total: ${sum(total_profit)}\n')
    writer.write(f'Average change: ${round(average_changes, 2)}\n')
    writer.write(f'Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase}\n')
    writer.write(f'Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease}\n')
