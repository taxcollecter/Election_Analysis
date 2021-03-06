# The data we need to retrieve.
# 1. The tota lnumber of votes cast
# 2 A complete list of candidates who received votes
# 3 The percentage of votes each candidate won
# 4 The total number of votes each candidate won
# 5 The winner of the election based on populaar vote.


import csv

# Assign a variable to load a file from a path.
file_to_load =  'C:\\Users\\lawof\\Desktop\\Bootcamp\\3\\election_results.csv'

# Assign a variable for the file to load and the path.
file_to_save = 'C:\\Users\\lawof\\Desktop\\Bootcamp\\3\\election_analysis\\analysis\\election_analysis.txt'

# 1. Initialize a total vote counter.
total_votes = 0
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


with open(file_to_load) as election_data:

 # To do: perform analysis.
    file_reader =  csv.reader(election_data)

# Read and print the header row.
    headers = next(file_reader)
    
    #print(headers)

    for row in file_reader:
   # 2. Add to the total vote count.
        total_votes +=  1
        candidate_name = row[2]
        #candidate_options.append(candidate_name)
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
        
            # 2. Begin tracking that candidate's vote count.
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



    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
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

        # 4. Print the candidate name and percentage of votes.
        #formattedVote = "{:.2f}".format(vote_percentage)
        #print(f"{candidate_name}: received {formattedVote}% of the vote.")

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    #print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)
    
    # Close the file.
    election_data.close()
