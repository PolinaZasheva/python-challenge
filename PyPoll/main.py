import os
import csv

#create new variables
number_votes = 0
candidates = []
total_votes = []

# open CSV file with raw data using a relative referene so the file can't be opened anywhere
csvpath = os.path.join('election_data.csv')
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

# Skip first row
    next(csvreader, None)

#Find the total number of votes
    for line in csvreader:
        number_votes = number_votes + 1

        candidate = line[2]

        #check if candidates has voted more than once
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            total_votes[candidate_index] = total_votes[candidate_index] + 1
        else:
            candidates.append(candidate)
            total_votes.append(1)

# calculated fields creation
percentage = []
max_votes = total_votes[0]
max_index = 0

# percent vote for each candidate and winner
for count in range(len(candidates)):
    vote_percent = total_votes[count]/number_votes*100
    percentage.append(vote_percent)
    if total_votes[count]>max_votes:
        max_votes = total_votes[count]
        print(max_votes)
        max_index = count
winner = candidates [max_index]

# Round
percentage = [round(i,2) for i in percentage]

 # Print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {number_votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentage[count]}% ({total_votes[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")