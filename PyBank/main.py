import os

import csv

budget_data_csv = os.path.join ("code","python-challenge","PyBank")

#Open and read csv
with open('Resources/budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Skip first row
    csv_header = next(csv_reader, None)
    
    #Define variables and lists
    month_count = 0
    profit_for_month = 0
    profit_for_prev_month = 0
    profit_diff = []
    month_list = []
    profit_total = 0

    
    for row in csv_reader:
        
        #Counts total number of months
        month_count += 1
        
        #Adds together monthly profit to calculate total profit for all months
        profit_for_month = int(row[1])
        profit_total += profit_for_month
        
        #Creates list of dates, skipping header row
        if month_count > 0:
            month_list.append(row[0])
        
        #Calculates change in profit between one month and the next, and then
        # creates a list of these values
        if month_count > 1:
            profit_diff.append(profit_for_month - profit_for_prev_month)

        #Sets value for previous month profit so that for next loop it 
        # can be subtracted off current month profit to find change in profit    
        profit_for_prev_month = profit_for_month

#Prints output as specified
print("Financial Analysis""\n"
"------------------------------""\n"
f'Total Months: {month_count}'"\n"
f'Total: ${profit_total}'"\n"
f'Average Change: ${round(sum(profit_diff)/(month_count-1),2)}'"\n"
f'Greatest Increase in Profits: {month_list[profit_diff.index(max(profit_diff))+1]} (${max(profit_diff)})'"\n"
f'Greatest Decrease in Profits: {month_list[profit_diff.index(min(profit_diff))+1]} (${min(profit_diff)})')

# export text file with results

textfile = 'Analysis/main_budget.txt'

# store text to be printed to a variable

output = ["Financial Analysis",
"------------------------------",
f'Total Months: {month_count}',
f'Total: ${profit_total}',
f'Average Change: ${round(sum(profit_diff)/(month_count-1),2)}',
f'Greatest Increase in Profits: {month_list[profit_diff.index(max(profit_diff))+1]} (${max(profit_diff)})',
f'Greatest Decrease in Profits: {month_list[profit_diff.index(min(profit_diff))+1]} (${min(profit_diff)})']

with open(textfile, 'w') as text:
    for elem in output:
        text.write(elem)
        text.write('\n')