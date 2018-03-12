'Create pathway and read data'
import os
import csv
election_files = ['election.csv', 'election_data_2.csv']
for fname in election_files:
    csvpath = os.path.join('raw_data', fname)
    #f.write(csvpath)
    with open(csvpath, newline='') as csvfile:
        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
       
    # Lists to store the data
    
    
        Voter_id = []
        County = []
        Candidates_dict = {}
        # Append data from the row
        Voter_id = [0]
        County = [1]
        Candidates_dict = {}

        Num_Votes =0

        for row in csvreader:
            if Num_Votes==0:
                Num_Votes+=1

                continue
            Num_Votes += 1
            # Candidate already in dict, add one
            if row[2] in Candidates_dict:
                Candidates_dict[row[2]]+=1
            else: #Candidate not in dict, so add it
                Candidates_dict[row[2]] = 1   
     
    # Subtract Header
    Num_Votes-=1 
    Winner = ''
    Max_percent = 0
    for candidate in Candidates_dict:
        percent = Candidates_dict[candidate]/Num_Votes
        percent *= 100
        if percent >  Max_percent:
            Winner = candidate
            Max_percent = percent 
        Candidates_dict[candidate] = [Candidates_dict[candidate],percent]




    print("Election Results")
    print("-----------------------------------")
    print("Total Votes: " + str(Num_Votes))
    print("-----------------------------------")
    print(Candidates_dict)
    for candidate in Candidates_dict:
        percent=Candidates_dict[candidate][1] 
        votes=Candidates_dict[candidate][0]
        print (candidate+": " + str(percent)+ \
        " ("+ str(votes)+")")
    print("-----------------------------------")
    print("Winner is " + Winner)


    filename= fname[0:-4] + ".txt"
    with open (filename,'w') as f:
        f.write("Election Results\n")
        f.write("-----------------------------------\n")
        f.write("Total Votes: " + str(Num_Votes)+"\n")
        f.write("-----------------------------------\n")
 
        for candidate in Candidates_dict:
            percent=Candidates_dict[candidate][1] 
            votes=Candidates_dict[candidate][0]
            f.write (candidate+": " + str(percent)+ " ("+ str(votes)+")\n")
        f.write("-----------------------------------\n")
        f.write("Winner is " + Winner)    