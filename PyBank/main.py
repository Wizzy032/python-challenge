# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
csvpath = os.path.join("Resources", "budget_data 2.csv")  # Input file path
output_path = os.path.join("analysis", "Financial_Analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
changes = []
months = []
previous_profit_loss = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Open and read the csv
with open(csvpath) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_profit_loss = int(first_row[1])

    # Track the total and net change


    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1

        # Track the net change
        total_net += int(row[1])
        change = int(row[1]) - previous_profit_loss
        changes.append(change)
        previous_profit_loss = int(row[1])
        months.append(row[0])
        # Calculate the greatest increase in profits (month and amount)
        if change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = change

        # Calculate the greatest decrease in losses (month and amount)
        if change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change


# Calculate the average net change across the months
average_change = sum(changes) / len(changes)

# Generate the output summary


# Print the output
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Write the results to a text file
with open(output_path, "w") as txt_file:
    txt_file.write("Financial_Analysis\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_net}\n")
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")