# Import relevent Python modules
from os import path
from collections import Counter
import csv


def Percentage(name, vote, index):
    '''Returns the portion of the vote for each candiate in percentage
        
            Parameters:
                name (str): Name of the candidate from the dict_list
                vote (int): The number of total vote each candidate recieved for dict_list
                index (int): The number of total votes in the data
                
            Retruns:
                Percent of vote is calculated and return as F-string in the following format:
                {name}: {percent to 3 decimal places}% {number of votes}
    '''
    percent = int(vote)/(index+1) * 100
    return f'{str(name)}: {percent:.3f}% ({vote})\n\n'


#Create variable for data in election_data.csv
cvspath =path.join("..", "Resources", "election_data.csv")


# Opens the file in read mode
with open(cvspath, encoding='UTF-8') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skips header in csv file and stores it in value "Header" 
    header = next(csvreader)

    Candidates = []
    #Creates a list with only the name of the candidates
    for index, row in enumerate (csvreader):
        Candidates.append(row[2])

# Counts the occurrence of each candidate and adds to dictionary_item 
Candidates_counts = Counter(Candidates)    

# Declare F-String variable to collect candidates information 
Candidates_info="" 
# Loops through dict_items to pass paramters to Percentage function
for name, num in Candidates_counts.items():
    Candidates_info += Percentage(name, num, index)
    

#Create F-String variable "result" to concatenate all strings
result = f'Election Results\n\n'\
        f'{"-"*55}\n\n'\
        f'Total Votes: {index+1}\n\n'\
        f'{"-"*55}\n\n'\
        f'{Candidates_info}'\
        f'{"-"*55}\n\n'\
        f'Winner: {max(Candidates_counts, key=Candidates_counts.get)}\n\n'\
        f'{"-"*55}\n\n'
print(result)
       
# Specify the file to write to and creates a new text file, "Results"
output_path = path.join("..", "Analysis", "Results.txt")

# Write F-string variable, Result, into text 
with open(output_path, 'w') as f:
    print(result, file=f)





