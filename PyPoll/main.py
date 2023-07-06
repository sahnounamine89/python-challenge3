import csv
import os

# Define the path to the CSV file
csvpath = os.path.join('..', 'Pybank', 'Resources', 'budget_data.csv')

# Initialize variables
total_months = 0
net_profit_losses = 0
prev_profit_loss = 0
profit_changes = []
greatest_increase = ['', 0]
greatest_decrease = ['', 0]

# Open the CSV file
with open(csvpath, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    # Iterate over each row in the CSV
    for row in reader:
        date = row[0]
        profit_loss = int(row[1])

        # Calculate the total number of months and net profit/losses
        total_months += 1
        net_profit_losses += profit_loss

        # Calculate the change in profit/losses and update the previous profit/loss
        change = profit_loss - prev_profit_loss
        prev_profit_loss = profit_loss

        # Skip the first month's data
        if total_months > 1:
            # Append the change to the profit_changes list
            profit_changes.append(change)

            # Find the greatest increase and decrease in profit/losses
            if change > greatest_increase[1]:
                greatest_increase = [date, change]
            if change < greatest_decrease[1]:
                greatest_decrease = [date, change]

# Calculate the average change in profit/losses
average_change = sum(profit_changes) / len(profit_changes)

# Print the results to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Define the path for the output text file
output_file = "financial_analysis.txt"

# Export the results to a text file
with open(output_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_profit_losses}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print a confirmation message
print(f"The financial analysis has been exported to {output_file}.")
