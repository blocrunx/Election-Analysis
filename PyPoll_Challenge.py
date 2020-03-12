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

# Challenge 2. Create a list for the counties
counties = []

# Challenge 3. Create a Dictionary
county_votes_dict = {}

# Challenge 4. Create a string to hold county name with largest turnout
winning_county = ""

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

        # Check if name already exists in the list
        if candidate_name not in candidate_options:
            #add the candidate name ot the candidate list.
            candidate_options.append(candidate_name)
            
            # Set candidate votes to zeor for new candidate
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] +=1

        # Challenge 5. Declare a variable to record number of votes a county received

        #Declare variable to add county name
        county_name = row[1]

        #Add county names to the the list
        if county_name not in counties:

            #add county name to the list of counties
            counties.append(county_name)

            #set county votes to 0 for new County
            county_votes_dict[county_name] = 0

        #incriment county's number of votes with each loop where it appears    
        county_votes_dict[county_name] += 1

    #save results to a text file
    with open(file_to_save, 'w') as txt_file:
        #Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"--------------------------\n")
        print(election_results, end="")
        #Save the final vote count to the text file
        txt_file.write(election_results)

        #iterate through the candidate list
        for candidate in candidate_votes:

            #retrieve the vote count for each candidate
            votes = candidate_votes[candidate]

            #Calculate vote percentage
            vote_percentage = int(votes)/int(total_votes)*100
            
            #assign candidate results to a variable 
            candidate_results = (f"{candidate}: {vote_percentage: .1f}% ({votes:,})\n")

            #print candidate results to terminal
            print(candidate_results)

            #print candidate_results to txt_file
            txt_file.write(candidate_results)
         


            #  To do: print out each candidate's name, vote count, and percentage of
            # votes to the terminal.
            #print(f"{candidate}: {vote_percentage: .1f}% ({votes:,})\n")

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
        

        #print(winning_candidate_summary)
    
        # Save the winning candidate's name to the text file.
        txt_file.write(winning_candidate_summary)

   