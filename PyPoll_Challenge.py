#The data we need to retreive
#total number of votes cast
#complete list of candidates who received votes
#total number of votes each candidate received
#percentage of votes each candidate won
#winner of the election based on popular vote

import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources/election_results.csv")

# Assign a variable to saev the file to a path
file_to_save = os.path.join('analysis', 'election_results.txt')

# Initialize a total vote counter
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

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Print each rown in the CSV file
    for row in file_reader:
        total_votes += 1

        # Print the canidate name from each row
        candidate_name = row[2]

        # Check if name already exists in the list
        if candidate_name not in candidate_options:
            
            # Add the candidate name ot the candidate list
            candidate_options.append(candidate_name)
            
            # Set candidate votes to zero for new candidate
            candidate_votes[candidate_name] = 0

        # Add a vote corresponding to the candidate's name in the dictionary
        candidate_votes[candidate_name] +=1

        # Challenge 5. Declare a variable to record number of votes a county received

        # Declare variable to add county name
        county_name = row[1]

        # Add county names to the list
        if county_name not in counties:

            # Add county name to the list of counties
            counties.append(county_name)

            # Set county votes to 0 for new county
            county_votes_dict[county_name] = 0

        # Incriment county's number of votes with each loop where it appears    
        county_votes_dict[county_name] += 1

    # Save results to a text file
    with open(file_to_save, 'w') as txt_file:
        
        # Print the final vote count to the terminal
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"--------------------------\n\n")
        print(election_results, end="")

        # Save the final vote count to the text file
        txt_file.write(election_results)
        
        # Create header for county section
        county_header = (f"County Votes:\n")
        txt_file.write(county_header)
        print(county_header)
    
        # Challenge 6. 
        # Iterate through county_votes_dict
        for county in county_votes_dict:
            
            # Assign votes county dictionary value
            votes = county_votes_dict[county]

            # Calculate percentage of vote
            vote_percentage = int(votes)/int(total_votes)*100

            # Assign county results to a variable
            county_results = (f"{county}: {vote_percentage: .1f}% ({votes:,})\n")
            
            # Print results to terminal
            print(county_results)

            # Write county % and votes to text file
            txt_file.write(county_results)

            # Find winning County Turnout
            if (votes > winning_count):
                winning_count = votes
                winning_county = county

        # Save winning county to variable and add formatting        
        winning_county_summary = (f"\n-------------------------\n"

        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n"
        )

        # Write winning county to text file 
        txt_file.write(winning_county_summary)

        # Print winning county to terminal
        print(winning_county_summary)
               
        # Reset variables for use with individual candidates
        winning_count = 0
        winning_percentage = 0
        

        # Iterate through the candidate dictionary
        for candidate in candidate_votes:

            # Retrieve the vote count for each candidate
            votes = candidate_votes[candidate]

            # Calculate vote percentage
            vote_percentage = int(votes)/int(total_votes)*100
            
            # Assign candidate results to a variable 
            candidate_results = (f"{candidate}: {vote_percentage: .1f}% ({votes:,})\n")

            # Print candidate results to terminal
            print(candidate_results)

            # Write candidate_results to txt_file
            txt_file.write(candidate_results)
            
            # Determine winning vote count and candidate
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true then set winning_count = votes and winning_percent =
                # vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage
                # And, set the winning_candidate equal to the candidate's name
                winning_candidate = candidate
            
        # Assign the winning candidate, their vote count and percentage to variable with 
        # following format:
        winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")
       
        # Write and print the winning candidate's name, vote count and vote percentage
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)

        
   