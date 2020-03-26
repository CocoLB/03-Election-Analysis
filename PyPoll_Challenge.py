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

# CHALLENGE Initialize and declare list and dictionnary of counties, and county with largest turnout
county_options = []
county_turnout = {}
largest_turnout_county = ""
largest_turnout = 0

# Track winning candidate, winning Count and percentage
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

        # CHALLENGE get the county nam,e from each row
        county_name = row[1]
        
        if candidate_name not in candidate_options:

            # Add candidate name to the list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # CHALLENGE get the list of counties, and votes per, in a similar manner
        if county_name not in county_options:

            # CHALLENGE add county name to the list
            county_options.append(county_name)

            # CHALLENGE begin tracking that county's vote count
            county_turnout[county_name] = 0

        # CHALLENGE add a vote to that county's count 
        county_turnout[county_name] += 1          


# Save the results to  our text file
with open(file_to_save, "w") as txt_file:

    # Print the final vote count
    election_results = (
        f"\nElection Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    # Save the final vote count to the text file
    txt_file.write(election_results)

    #CHALLENGE determine the percentage of votes for each county by looping through the counties
    for county in county_turnout:
        # CHALLENGE retrieve vote count (turnout) per county
        turnout = county_turnout[county]
        # CHALLENGE calculate the percentage
        turnout_percentage = float(turnout) / float(total_votes)*100
        # CHALLENGE print couny names and turnout percentage and save to txt file
        county_results = (f"{county}: {turnout_percentage:.1f}% ({turnout:,})\n")
        print(county_results)
        txt_file.write(county_results)

        #CHALLENGE gettting the county with largest turnout as well as its percentage and turnout
        if (turnout > largest_turnout):
            largest_turnout = turnout
            largest_turnout_county = county

    # CHALLENGE print, and save to text file, county with larghest turnout
    largest_turnout_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_turnout_county}\n"
        f"-------------------------\n")
    print(largest_turnout_county_summary)
    txt_file.write(largest_turnout_county_summary)

    # Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through the candidate list
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes)*100
        # Print the candidate name and percentage of votes to terminal and save to txt file
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)


        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If  true then set winning_count=votes and winning_percentage=vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And set the winning_candidate equal to the candidate's name
            winning_candidate = candidate
    # Print the winning candidate's results        
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}\n"
        f"-------------------------\n")
    print(winning_candidate_summary) 

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)  







      

    







    










