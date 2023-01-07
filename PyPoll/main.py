import os

import csv

# File path for csv
election_data_csv = os.path.join ("code/python-challenge/PyPoll")

# Open and read csv
with open('Resources/election_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader, None)

    # Define variables and lists
    total_votes = 0
    candidates = []
    candidate_list = []
    candidate_votecount = {}
    
    for row in csv_reader:
        
        # sum rows to count total votes        
        total_votes += 1

        #create list of all candidates (with duplicates)
        candidate_list.append(row[2])

    # Loop through candidate list with duplicates and create new list 
    # of candidates without duplicates
    
    for i in candidate_list:
        if i not in candidates:
            candidates.append(i)

        # Loop though candiate list and create a dictionary that counts
        # and assigns votes to each candidate        
        if i not in candidate_votecount:
            candidate_votecount[i] = 1
        else:
            candidate_votecount[i] +=1

    # Calculate votes per candidate as a percentage of total votes cast.
    # Round to 3 decimal places        
    charles_pct = (candidate_votecount["Charles Casper Stockham"]/total_votes)*100
    charles_pct = round(charles_pct,3)
    diana_pct = (candidate_votecount["Diana DeGette"]/total_votes)*100
    diana_pct = round(diana_pct,3)
    raymon_pct = (candidate_votecount["Raymon Anthony Doane"]/total_votes)*100
    raymon_pct = round(raymon_pct,3)

# Output of results
print("Election Results""\n"
"----------------------------""\n"
f'Total Votes: {total_votes}''\n'
"----------------------------""\n"
f'{candidates[0]}: {charles_pct}% ({candidate_votecount["Charles Casper Stockham"]})''\n'
f'{candidates[1]}: {diana_pct}% ({candidate_votecount["Diana DeGette"]})''\n'
f'{candidates[2]}: {raymon_pct}% ({candidate_votecount["Raymon Anthony Doane"]})''\n'
"----------------------------""\n"
f'Winner: {max(candidate_votecount, key=candidate_votecount.get)}''\n'
"----------------------------")

# export text file with results

textfile = 'Analysis/main_election.txt'

# store text to be printed to a variable

output = ["Election Results""\n"
"----------------------------""\n"
f'Total Votes: {total_votes}''\n'
"----------------------------""\n"
f'{candidates[0]}: {charles_pct}% ({candidate_votecount["Charles Casper Stockham"]})''\n'
f'{candidates[1]}: {diana_pct}% ({candidate_votecount["Diana DeGette"]})''\n'
f'{candidates[2]}: {raymon_pct}% ({candidate_votecount["Raymon Anthony Doane"]})''\n'
"----------------------------""\n"
f'Winner: {max(candidate_votecount, key=candidate_votecount.get)}''\n'
"----------------------------"]

with open(textfile, 'w') as text:
    for elem in output:
        text.write(elem)
        text.write('\n')

