#The data we need to retreive
#total number of votes cast
#complete list of candidates who received votes
#total number of votes each candidate received
#percentage of votes each candidate won
#winner of the election based on popular vote

import csv
import os

file_to_load = os.path.join("Resources/election_results.csv")
file_to_save = os.path.join('analysis', 'election_analysis.txt')

with open(file_to_load) as election_data:

    #to-do read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #print each row in the CSV file
    headers = next(file_reader)
    print(headers)

   