#modules
import csv

#get file path
data_file_path = "PyPoll/Resources/election_data.csv"

#set variables

total_votes = 0
candidates = []
candidate_votes = []
vote_sections = []

#open results
with open (data_file_path) as results:
    results_reader=csv.reader(results)
    for vote in results:
        total_votes +=1
    print (total_votes)
#read results

#print results

##print ("Election Results")
##print ("-------------------------")
##print ("Total Votes: <votes_total")
##print ("-------------------------")
##print ("<cand1_name>: <cand1_percent>% (<cand1_vote_count>)")
##print ("-------------------------")
##print ("Winner: <winner_name")
##print ("------------------------")

#export results