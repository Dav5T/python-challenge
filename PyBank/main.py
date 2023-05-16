import os
import csv


cvspath = os.path.join("..", "Resources", "budget_data.csv")
Total_Profit_Losses = 0
Total_changes = 0
Changes = {}
Changes = dict()

#opens CSV file 
with open(cvspath, encoding='UTF8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
	 
    prev = 0
    for index, row in enumerate(csvreader):
        
        #Calculate the overall profits
        Total_Profit_Losses += int(row[1])
         
         #Calculate the change in profit/loss over each month 
        change = int(row[1]) - int(prev)

        if prev!= row[1]:
            prev = row [1]
        
        if index == 0:
            dict ={row[0] : 0}
            Changes.update(dict)
        else:
            dict ={row[0] : change}
            Changes.update(dict)

    
    print(f'Financial Anlysis')

    print(f'Total Month: {index+1}')
    print(f'Total: ${Total_Profit_Losses}')
    print(f'Average Change: ${sum(Changes.values())/index:.2f}')
    print(f"Greatest Increase in Profits: {max(Changes, key=Changes.get)} (${max(Changes.values())})")
    print(f"Greatest Decrease in Profits: {min(Changes, key=Changes.get)} (${min(Changes.values())})")
   