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

# Open the election results and read the file
with open(file_to_load) as election_data:
    
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Read and print the header row
    headers = next(file_reader)
    print(headers)







    










