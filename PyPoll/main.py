# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
csvpath = os.path.join("Resources", "election_data.csv")  # Input file path
output_path = os.path.join("analysis", "election_results.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(csvpath, mode='r') as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        total_votes += 1
        candidate = row[2]  # Candidate's name is in the third column
        
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}
winner = max(candidate_votes, key=candidate_votes.get)
# Print a loading indicator (for large datasets) and print the output
print(". ", end="")
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Open a text file to save the output
with open(output_path, mode='w') as txt_file:

    results = ("Election Results\n"
        "-------------------------\n"
        f"Total Votes: {total_votes}\n"
        "-------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = candidate_percentages[candidate]
        candidate_result = f"{candidate}: {percentage:.3f}% ({votes})\n"
        results += candidate_result
    results += (
        "-------------------------\n"
        f"Winner: {winner}\n"
        "-------------------------\n")
    
    # Write the results to a text file
    txt_file.write(results)
