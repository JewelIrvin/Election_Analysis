# Assign a variable for the file to load and the path
import csv
import os

# Assign a variable to load a file from a path.

file_to_load = "election_results.csv"

# Assign a variable to save the file to a path.

file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Declare dictornary and list
candidate_options = []
candidate_votes = {}
# Open the election results and read the file


with open(file_to_load) as election_data:

 # To do: read and analyze the data here.
    file_reader = csv.reader(election_data) 

# Print each row in the CSV file.
    headers = next(file_reader)

    for row in file_reader:
        
        total_votes += 1
        
        candidate_name = row[2]
        
                # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1      
# Save the results to our text file.       
with open(file_to_save, "w") as txt_file:
    
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n") 
    print(election_results, end="")
    
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
    
        votes = candidate_votes[candidate_name]
    
        vote_percentage = float(votes) / float(total_votes) * 100
    
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

# Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
#  Save the candidate results to our text file.
        txt_file.write(candidate_results)
    
# Determine winning vote count and candidate
# 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
     # 2. If true then set winning_count = votes and winning_percent =
     # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
     # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    
    
# To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.
    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)