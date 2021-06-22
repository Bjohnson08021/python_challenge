import os
import csv

csvpath = os.path.join('.' ,'Resources', 'election_data.csv')
 #setting variable
total_votes = 0
Khan = 0
Correy = 0
Li = 0
OToole = 0

with open(csvpath) as csvfile:

   # csv_reader = csv.reader(csv_file)
    csvreader= csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    
    
    
    #Candidate vote count
    for row in csvreader:
        
        total_votes = total_votes + 1
        if (row[2]) == ("Khan"):
            Khan = Khan + 1
        elif (row[2]) == ("Correy"):
            Correy = Correy + 1
        elif (row[2]) == ("Li"):
            Li = Li + 1
        else:
            OToole = OToole + 1
#Getting the percentage
    Khan_total = Khan / total_votes * 100
    Correy_total = Correy / total_votes * 100
    Li_total = Li / total_votes * 100
    OToole_total = OToole / total_votes * 100

#using condtions to determine the winner
if Khan > Correy and Khan > Li and Khan > OToole:
    Winner = "Khan"

elif Correy > Khan and Correy > Li and Correy > OToole:
    Winner = "Correy" 

elif Li > Khan and Li > Correy and Li > OToole:
    Winner = "Li"    

elif OToole > Khan and OToole > Correy and OToole > Li:
    Winner = OToole
        #`Candidate_list = Candidate_list + 1
#print statement and percentage
print(f"Election Resluts") 
print(f"-------------------")
print(f"Total votes: {total_votes}")
print(f"---------------------------")
print(f"Khan: {round(Khan_total,2)}% ({Khan})")
print(f"Correy: {round(Correy_total,2)}% ({Correy})")
print(f"Li: {round(Li_total,2)}% ({Li})")
print(f"OToole: {round(OToole_total,2)}% ({OToole})")
print("-------------------------------------")
print(f"Winner: {Winner}")
print("-------------------------------------")      

output_path =("election.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as text_file: 


    text_file.write("Election Results")
    text_file.write('\n')
    text_file.write("-------------------------------------")
    text_file.write('\n')
    text_file.write(f"Total votes: {total_votes}")
    text_file.write('\n')
    text_file.write("-------------------------------------")
    text_file.write('\n')
    text_file.write(f"Khan: {round(Khan_total,2)}% ({Khan})")
    text_file.write('\n')
    text_file.write(f"Correy: {round(Correy_total,2)}% ({Correy})")
    text_file.write('\n')
    text_file.write(f"Li: {round(Li_total,2)}% ({Li})")
    text_file.write('\n')
    text_file.write(f"OToole: {round(OToole_total,2)}% ({OToole})")
    text_file.write('\n')
    text_file.write("-------------------------------------")
    text_file.write('\n')
    text_file.write(f"Winner: {Winner}")
    text_file.write('\n')
    text_file.write("-------------------------------------")