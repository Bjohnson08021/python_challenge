
import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_Data.csv')
 
total_months = 1
sum_change = 0 



with open(csvpath) as csvfile:

   # csv_reader = csv.reader(csv_file) use delimiter to split ,
    csvreader= csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    row = next(csvreader)
#setting the variables
    total_amount = int(row[1])
    opening_profit = int(row[1])
    last_month = opening_profit
    greatest_increase = int(row[1])
    greatest_increase_date = row[0]
    greatest_decrease = int(row[1])
    greatest_decrease_date = row[0]


    for row in csvreader:
       #setting loops for these variables
        total_months = total_months + 1
        opening_profit = int(row[1])
        total_amount = total_amount + opening_profit
       #setting profit change
        change = opening_profit - last_month
        sum_change = sum_change + change
        average_change = sum_change/(total_months-1)
       #The overall greatest increase in profit with date 
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = row [0]
       #The overall greatest decrease in profit with date
        if change < greatest_decrease:
            greatest_decrease = change 
            greatest_decrease_date = row[0]

        last_month = opening_profit

        print("Financial Analysis")
        print("Total Months:" + str(total_months))
        print("Total amount:" + "$" + str(total_amount))
        print(f"Average Change: $ {round(average_change,2)}")
        print(f"Greatest Increase: {greatest_increase_date} ${greatest_increase}")
        print(f"Greatest Decrease: {greatest_decrease_date} ${greatest_decrease}")



output_path =("budget.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as text_file:
    
    
    # Write the first row (column headers)
    text_file.write("Financial Analysis")
    text_file.write('\n')
    text_file.write("-------------------------------------")
    text_file.write('\n')
    text_file.write("Total Months:" + str(total_months))
    text_file.write('\n')
    text_file.write("Total amount:" + "$" + str(total_amount))
    text_file.write('\n')
    text_file.write(f"Average Change: $ {round(average_change,2)}")
    text_file.write('\n')
    text_file.write(f"Greatest Increase: {greatest_increase_date} ${greatest_increase}")
    text_file.write('\n')
    text_file.write(f"Greatest Decrease: {greatest_decrease_date} ${greatest_decrease}")
    
    