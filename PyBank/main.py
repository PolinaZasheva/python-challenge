import os
import csv

#create variables for calculations
month_counter = 0
total_revenue = 0
total_revenue_change = 0

# open CSV file with raw data using a relative referene so the file can't be opened anywhere
csvpath = os.path.join('budget_data.csv')
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

# Skip headers
    next(csvreader, None)

 # Start reading file at line 1
    line = next(csvreader,None)
    max_month = line[0]
    min_month = line[0]
    revenue = float(line[1])
    previous_revenue = revenue
    min_revenue = revenue
    max_revenue = revenue
    month_counter = 1
    total_revenue = float(line[1])
    total_revenue_change = 0

# Read one line at a time
    for line in csvreader:

        
        month_counter = month_counter + 1
        revenue = float(line[1])

        # Total Revenue Calculation
        total_revenue = total_revenue + revenue

        # change revenue calculation
        revenue_change = revenue - previous_revenue

        # aggregate change calculation
        total_revenue_change = total_revenue_change + revenue_change

        # Min/ Max determination
        if revenue_change > max_revenue:
            max_month = line[0]
            max_revenue = revenue_change

        if revenue_change < min_revenue:
            min_month = line[0]
            min_revenue = revenue_change

        # Set previous revenue 
        previous_revenue = revenue

    # Finish calculations
    average_revenue = total_revenue/month_counter
    average_revenue_change = total_revenue_change/(month_counter-1)

    # Round decimal
    total_revenue = int(total_revenue)
    average_revenue_change = int(average_revenue_change)
    max_revenue = int(max_revenue)
    min_revenue = int(min_revenue)

    # Print analysis
    print(f"Financial Analysis:")
    print("-------------------------------------------------------")
    print(f"Total Months: {month_counter}")
    print(f"Total: {total_revenue} USD")
    print(f"Average Change: {average_revenue_change} USD")
    print(f"Greatest Increase in Profits: {max_month} {max_revenue} USD")
    print(f"Greatest Decrease in Profits: {min_month} {min_revenue} USD")
    print("")

    # Export a text file with the results
    output_file = budget_revenue[0:-4]

    write_budget_revenue = f"{output_file}_pybank_results.txt"

    # Open write file
    filewriter = open(write_budget_revenue, mode = 'w')

    # Print to write file
    filewriter.write(f"Financial Analysis:\n")
    filewriter.write("-------------------------------------------------------\n")
    filewriter.write(f"Total Months: {month_counter}\n")
    filewriter.write(f"Total: {total_revenue} USD\n")
    filewriter.write(f"Average Change: {average_revenue_change} USD\n")
    filewriter.write(f"Greatest Increase in Profits: {max_month} {max_revenue} USD\n")
    filewriter.write(f"Greatest Decrease in Profits: {min_month} {min_revenue} USD\n")
    filewriter.write("")

    filewriter.close()




