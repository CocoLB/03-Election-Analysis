# The data we need to retrieve
# 1. The total num,ber of votes cast
# 2. A compolete list of the candidates who received votes
# 3. The total number of votes each candidates won
# 4. The percentage of votes each candidates won 
# 5. The winner of the election based on popular vote

# Add dependencies
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter & declare a new list of candidates, a new dictionnary
total_votes = 0
candidate_options = []
candidate_votes={}

# Winning candidate and winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results
with open(file_to_load) as election_data:
    
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Read the header row
    headers = next(file_reader)
    
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:

            # Add candidate name to the list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts
# Iterate through the candidate list
for candidate in candidate_votes:
    # Retrieve vote count of a candidate
    votes = candidate_votes[candidate]
    # Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes)*100
    # Print the candidate name and percentage of votes
    print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If  true then set winning_count=votes and winning_percentage=vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # And set the winning_candidate equal to the candidate's name
        winning_candidate = candidate
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}\n"
    f"-------------------------\n")
print(winning_candidate_summary)   







      

    







    










