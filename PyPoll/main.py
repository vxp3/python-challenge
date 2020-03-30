import os
import csv
from pathlib import Path

#Declare Variables for vote
cVotes = 0
kVotes = 0
lVotes = 0 
oVotes = 0
totalVotes = 0

#Have it open the csv file budget_dat from the folder Resources
electionData = os.path.join("Resources", "election_data.csv")

#CSV reader and variable that hold contents
with open(electionData) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    #Calculate total number of votes cast
    for row in reader:
        totalVotes += 1
        #Do if statement, count thru the row and not else it will count other and add to it for each candidates
        if row[2] == "Correy":
            cVotes = cVotes + 1
        elif row[2] == "Khan":
            kVotes = kVotes + 1
        elif row[2] == "Li": 
            lVotes =  lVotes + 1
        else :
            oVotes = oVotes + 1

#Do the percentage of votes each candidate won
#Candidates% = (Candidates Votes / total votes) * 100
C = (cVotes/totalVotes) * 100
K = (kVotes/totalVotes) * 100
L = (lVotes/totalVotes) * 100
O = (oVotes/totalVotes) * 100

#Round the number up to %
rC = round(C, 3)
rK = round(K, 3)
rL = round(L, 3)
rO = round(O, 3)

#Do if count, tally the winner and produce the winner
if cVotes > kVotes > lVotes > oVotes:
    Winner = "Correy"
elif kVotes > cVotes > lVotes > oVotes:
    Winner = "Khan"
elif lVotes > oVotes > kVotes > cVotes:
    Winner = "Li"
else:
    Winner = "O'Tooley"

#Print display information
print("Election Results")
print("----------------")
print("Total Votes: " + str(totalVotes))
print("----------------")
print("Khan: " + str(rK) + "%" + " " + "(" + str(kVotes) + ")")
print("Correy: " + str(rC) + "%" + " " + "(" + str(cVotes) + ")")
print("Li: " + str(rL) + "%" + " " + "(" + str(lVotes) + ")")
print("O'Tooley: " + str(rO) + "%" + " " + "(" + str(oVotes) + ")")
print("----------------")
print("Winner: " + str(Winner))
print("----------------")

#Output files
outputFile = Path("Election Result.txt")

with open(outputFile, "w") as f:
#Write to file Election Results.txt
    f.write("Election Results")
    f.write("----------------")
    f.write("Total Votes: " + str(totalVotes))
    f.write("----------------")
    f.write("Khan: " + str(rK) + "%" + " " + "(" + str(kVotes) + ")")
    f.write("Correy: " + str(rC) + "%" + " " + "(" + str(cVotes) + ")")
    f.write("Li: " + str(rL) + "%" + " " + "(" + str(lVotes) + ")")
    f.write("O'Tooley: " + str(rO) + "%" + " " + "(" + str(oVotes) + ")")
    f.write("----------------")
    f.write("Winner: " + str(Winner))
    f.write("----------------")