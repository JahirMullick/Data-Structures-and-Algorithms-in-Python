from datetime import date
import csv


dt = date.today()
dt = dt.strftime('%d/%m/%y')
file_name = "test.csv"
csvFile = "Log.csv"

# Open the file and add some data

with open(file_name, 'w') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow([dt])
file.close()

exp = []
stopped = False

with open(csvFile, 'a') as filew:
    csvwriter = csv.writer(filew)
    while not stopped:
        xp = int(input('What is the expense (type 0 to stop): '))
        if xp == 0:
            stopped = True
        else:
            csvwriter.writerow([dt,xp])
            exp.append(xp)
filew.close()
print('Your expenses today are:- ', exp)
print('Your total is:- ', sum(exp))
