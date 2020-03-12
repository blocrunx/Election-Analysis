#The data we need to retreive
#total number of votes cast
#complete list of candidates who received votes
#total number of votes each candidate received
#percentage of votes each candidate won
#winner of the election based on popular vote

import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")

# Assign a variable to saev the file to a path.
file_to_save = os.path.join('analysis', 'election_analysis.txt')

#initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Create dictionary to hold candidate votes
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    #to-do read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Print each rown in the CSV file
    for row in file_reader:
        total_votes += 1

        # print the canidate name from each row
        candidate_name = row[2]

        #check if name already exists in the list
        if candidate_name not in candidate_options:
            #add the candidate name ot the candidate list.
            candidate_options.append(candidate_name)
            
            # set candidate votes to zeor for new candidate
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] +=1

    #iterate through the candidate list
    for candidate in candidate_votes:

        #retrieve the vote count for each candidate
        votes = candidate_votes[candidate]

        #Calculate vote percentage
        vote_percentage = int(votes)/int(total_votes)*100


        #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        print(f"{candidate}: {vote_percentage: .1f}% ({votes:,})\n")

        # Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
             # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate

        # To do: print out the winning candidate, vote count and percentage to
        # terminal.

    winning_candidate_summary = (
    f"--------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"--------------------------\n")

    print(winning_candidate_summary)
    
   

   