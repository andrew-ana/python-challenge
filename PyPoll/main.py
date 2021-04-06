## OMIMP
## Andrew Anastasiades

#  O   M   I   M   P  
#  H   A       I   A  
#      N       S   N
#              S   D
#                  A
#                  S

## DEPENDENCIES
import os
import csv

## FILE PATHS
election_data_path = os.path.join("Resources", "election_data.csv") #Election Data File Path
results_file_path = os.path.join("Analysis","Election Results.txt")

##READ FILE
data_list = list() #List to hold rows #OMIMP
with open(election_data_path) as election_file:
    csvreader = csv.reader(election_file, delimiter=',') #Reader Object
    header = next(csvreader) # Get Column Heads #OMIMP
    for row in csvreader:
        data_list.append(row)
    #Now we can close File

## ANALYZE DATA
# List Comprehensions to make life easier
id_list = [row[0] for row in data_list]
county_list = [row[1] for row in data_list]
cand_list = [row[2] for row in data_list]
#Results
total_votes = len(data_list) #totals
candidates = list(set(cand_list)) #Make a list of unique Candidates
votes_by_cand = [cand_list.count(candidate) for candidate in candidates] #Make a list of vote totals
percent_by_cand = [(votes/total_votes)*100 for votes in votes_by_cand] #Make a list of %s
#Let's Consolidate the lists so we can sort (also I am now formatting my %s)
result_list = [[candidates[i], votes_by_cand[i], "{:.3f}".format(percent_by_cand[i])] for i in range(len(candidates))]
#Ok, I admit we haven't covered lamba yet, but this is an easy way to sort a list of lists.
#   If I HAVE to use only what we've covered so far I could build a dictionary or 
#   find the max value of the vote list and pop that from each of the lists, then reiterate through,
#   popping that max value. But is that really worth the time?
sorted_results = sorted(result_list, key=lambda x : x[1], reverse=True)
winner = sorted_results[0][0]

##WRITE RESULTS 
with open(results_file_path, "w") as results:
    
    results.write(f"Election Results")
    results.write("\n")
    print(f"Election Results")
    
    results.write(f"--------------------------")
    results.write("\n")
    print(f"--------------------------")
    
    results.write(f"Total Votes: {total_votes}")
    results.write("\n")
    print(f"Total Votes: {total_votes}")
    
    results.write(f"--------------------------")
    results.write("\n")
    print(f"--------------------------")
    
    for each in sorted_results:
        results.write(f"{each[0]}: {each[2]}% ({each[1]})")
        results.write("\n")
        print(f"{each[0]}: {each[2]}% ({each[1]})")

    results.write(f"--------------------------")
    results.write("\n")
    print(f"--------------------------")
    
    results.write(f"Winner: {winner}")
    results.write("\n")
    print(f"Winner: {winner}")
    
    results.write(f"--------------------------")
    results.write("\n")
    print(f"--------------------------")
## END