#Have it run on all platform
import os

#Import library
import csv
from pathlib import Path

#Declare variable
greatestLoss = ["", ""]
greatestProfit = ["", ""]
prevGreatest = 0
prevLess = 0
profitChange = 0
prevProfit = 0 
totalMonth = 0
totalNet = 0
totalProfitChange = 0

#Improved reading using cvs module
#Have it open the csv file budget_dat from the folder Resources
budgetData = os.path.join("Resources", "budget_data.csv")

#CSV reader and variable that hold contents
with open(budgetData) as csvfile:
    reader = csv.reader(csvfile)
    #Add header
    header = next(reader)
    #Calculate total months
    for row in reader:
        totalMonth += 1 
        #Calculate total net
        totalNet += int(row[1])
        #Average of change in profit/losses" over the entire period
        #Take the previous month - the 2nd month to find the difference and loop 
        totalProfitChange += profitChange
        profitChange =  int(row[1]) - prevProfit
        prevProfit = int(row[1])
        #Calculate greatest increase and greatest decrease in profits
        #Do a if loop
        #Find the less or the greatest change
        if (prevGreatest < profitChange ):
            greatestProfit = [row[0], str(profitChange)]
            prevGreatest = profitChange

        if (prevLess > profitChange ):
            greatestLoss = [row[0], str(profitChange)]
            prevLess = profitChange

#Find out the average change
average = totalProfitChange / totalMonth

#Print display information

print("Financial Analysis")
print("-------------------")
print("Total months: " + str(totalMonth))
print("Total profit: " + "$" + str(totalNet))
print("Average profit: " + str(average)) 
#I dont know why I can't get the math to come out right
print("Greatest Increase in Profits: " + str(greatestProfit))
print("Greatest Decrease in Profits: " + str(greatestLoss))

#Output files
outputFile = Path("Financial Analysis Summary.txt")

with open(outputFile, "w") as f:
#Write to file Financial Analysis Summary.txt 
#Use \n to write newline in a file
    f.write("Financial Analysis")
    f.write("\n")
    f.write("------------------")
    f.write("\n")
    f.write("Total months: " + str(totalMonth))
    f.write("\n")
    f.write("Total profit: " + "$" + str(totalNet))
    f.write("\n")
    f.write("Average profit: " + str(average))
    f.write("\n")
    f.write("Greatest Increase in Profits: " + str(greatestProfit))
    f.write("\n")
    f.write("Greatest Decrease in Profits: " + str(greatestLoss))
