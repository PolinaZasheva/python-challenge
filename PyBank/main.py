import os
import csv

#create new variables
month_counter = 0
total_profit = 0
total_profit_change = 0

# open CSV file with raw data using a relative referene so the file can't be opened anywhere
csvpath = os.path.join('budget_data.csv')
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

# Skip first row
    next(csvreader, None)

 # Start reading file at line 1
    line = next(csvreader,None)
    max_month = line[0]
    min_month = line[0]
    profit = float(line[1])
    previous_profit = profit
    min_profit = profit
    max_profit = profit
    month_counter = 1
    total_profit = float(line[1])
    total_profit_change = 0

# Read one line at a time
    for line in csvreader:

        
        month_counter = month_counter + 1
        profit = float(line[1])

        # Total Profit Calculation
        total_profit= total_profit + profit

        # change profit calculation
        profit_change = profit- previous_profit

        # aggregate change calculation
        total_profit_change = total_profit_change + profit_change

        # Min/ Max determination
        if profit_change > max_profit:
            max_month = line[0]
            max_profit = profit_change

        if profit_change < min_profit:
            min_month = line[0]
            min_profit = profit_change

        # Set previous profit 
        previous_profit = profit

    # Finish calculations
    average_profit = total_profit/month_counter
    average_profit_change = total_profit_change/(month_counter-1)

    # Round decimal
    total_profit = int(total_profit)
    average_profit_change = int(average_profit_change)
    max_revenue = int(max_profit)
    min_revenue = int(min_profit)

    # Print analysis
    print(f"Financial Analysis:")
    print("-------------------------------------------------------")
    print(f"Total Months: {month_counter}")
    print(f"Total: {total_profit} USD")
    print(f"Average Change: {average_profit_change} USD")
    print(f"Greatest Increase in Profits: {max_month} {max_revenue} USD")
    print(f"Greatest Decrease in Profits: {min_month} {min_revenue} USD")
    print("")

output_file = ("PyBank.txt")
write_file = f"{output_file}_Results.txt"

# Write file
filewrite = open(write_file, mode = 'w')

# Print to write file
filewrite.write(f"Financial Analysis:\n")
filewrite.write("________________________________\n")
filewrite.write(f"Total Months: {month_counter}\n")
filewrite.write(f"Total: {total_profit} USD\n")
filewrite.write(f"Average Change: {average_profit_change} USD\n")
filewrite.write(f"Greatest Increase in Profits: {max_month} {max_revenue} USD\n")
filewrite.write(f"Greatest Decrease in Profits: {min_month} {min_revenue} USD\n")
filewrite.write("")

filewrite.close()

