# Required to read and write files 
from os import path
import csv

# create variable for data in budget_data.csv
cvspath = path.join("..", "Resources", "budget_data.csv")


Total_Profit_Losses = 0
New_list = {}
New_list = dict()

# opens the file in read mode
with open(cvspath, encoding='UTF-8') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    # Stores the header and skips it   
    header = next(csvreader)
	
    # Declare variable for previous row to find change in Profit/Loss
    prev_row = 0

    # Loop through all the remaining rows in the file 
    for index, row in enumerate(csvreader):
        
        # Calculates the overall Profit/Loss
        Total_Profit_Losses += int(row[1])
         
        # Calculate the change in Profit/Loss for each month 
        Monthly_change = int(row[1]) - int(prev_row)

        # Sets the value prev_row variable 
        if prev_row!= row[1]:
            prev_row = row [1]
        
        # First month doesn't have a monthly change; no previous month to compare
        # Sets the first value for the key to 0 in New_list dictionary
        if index == 0:
            dict ={row[0] : 0}
            New_list.update(dict)
        # Adds new key-value pair from the remaining rows
        else:
            dict ={row[0] : Monthly_change}
            New_list.update(dict)
    
    # Variable, "result", concatenates F-strings
    result = f'Financial Anlysis\n\n'\
             f'{"-"*45}\n\n'\
             f'Total Month: {index+1}\n\n'\
             f'Total: ${Total_Profit_Losses}\n\n'\
             f'Average Change: ${sum(New_list.values())/index:.2f}\n\n'\
             f'Greatest Increase in Profits: {max(New_list, key=New_list.get)} (${max(New_list.values())})\n\n'\
             f'Greatest Decrease in Profits: {min(New_list, key=New_list.get)} (${min(New_list.values())})\n\n'   

    print (result)

# Specify where to create new text file, Results
output_path = path.join("..", "Analysis", "Results.txt")
with open(output_path, 'w') as f:
    # writes f-string, "result", to new text file
    print(result, file=f)
    

