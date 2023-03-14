# Module for statistics - easier than doing the math!
import statistics     
from csv import reader
print('*** Read Budget Data ***')
# skip first line i.e. read header first and then iterate over each row od csv as a list
monthCount = 0
totalVolume = 0
greatestIncrease = 0
bestMonth = ''
greatestDecrease = 0
worstMonth = ''

change = []
monthToMonthChange = []

with open('budget_data.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    # Check file as empty
    if header != None:
        # Iterate over each row after the header in the csv
        for row in csv_reader:
           #print("Date :" + str(row[0]) + " , Profit/Loss : " + str(row[1]))          
           monthCount += 1
           totalVolume += int(row[1])
           if int(row[1]) > greatestIncrease:
               bestMonth = (row[0])
               greatestIncrease = int(row[1])
           elif int(row[1]) < greatestDecrease:
               worstMonth = (row[0])
               greatestDecrease = int(row[1])
           change.append(int(row[1]))
           

# track monthly changes
for i in range(len(change)-1):
    monthlyChange = (change[i+1] - change[i])
    monthToMonthChange.append(monthlyChange)   

averageChange = statistics.mean(monthToMonthChange)

print("Financial Analysis Data")
print("___________________________________")

print("Total No of Months: " + str(monthCount))
print("Average Change is: $" + str(round(averageChange, 2)))
print("Total: $" + str(totalVolume))
print("Greatest Increase in Profits: " + str(bestMonth) + "  ($" + str(greatestIncrease) + ")")
print("Greatest Decrease in Profits: " + str(worstMonth) + "  ($" + str(greatestDecrease) + ")")

# now write this to an output file
f = open("financial_analysis_data.txt", "w")
f.write("Financial Analysis\n")
f.write("___________________________________\n")

f.write("\nTotal No of  Months: " + str(monthCount))
f.write("\nAverage Change is: $" + str(round(averageChange, 2)))
f.write("\nTotal: $" + str(totalVolume))
f.write("\nGreatest Increase in Profits: " + str(bestMonth) + "  ($" + str(greatestIncrease) + ")")
f.write("\nGreatest Decrease in Profits: " + str(worstMonth) + "  ($" + str(greatestDecrease) + ")")

           