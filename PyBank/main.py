import os
import csv

# Define the path to the input file
csv_path = os.path.join('..', 'Pypoll', 'Resources', 'election_data.csv')

# Initialize variables
total_votes = 0
candidates = {}
winner_name = ""

# Read the CSV file
with open(csv_path, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Skip the header row
    next(csv_reader)
    
    # Count the votes
    for row in csv_reader:
        total_votes += 1
        candidate_name = row[2]
        
        # Add the candidate to the candidates dictionary
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        else:
            candidates[candidate_name] += 1

# Create a text file to write the analysis results
output_file = "election_results.txt"

# Open the file in write mode
with open(output_file, 'w') as file:
    
    # Write the election results to the file
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    
    # Calculate and write the percentage of votes and total votes for each candidate
    for candidate_name, vote_count in candidates.items():
        percentage = (vote_count / total_votes) * 100
        file.write(f"{candidate_name}: {percentage:.3f}% ({vote_count})\n")
        
        # Check if the current candidate has the most votes
        if winner_name == "" or vote_count > candidates[winner_name]:
            winner_name = candidate_name
    
    file.write("-------------------------\n")
    file.write(f"Winner: {winner_name}\n")
    file.write("-------------------------\n")

# Print the analysis to the terminal
with open(output_file, 'r') as file:
    print(file.read())
