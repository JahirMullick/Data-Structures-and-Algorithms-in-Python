'''
Connect to mysql using python 
and import the csv file into mysql 
and create a table.


System requirements :
Install the pydrive python module as follows :
pip install mysql-connector-python
pip install pandas

Install MySQL : 
MySQL Workbench with mysql
'''


# import csv
 
# with open('Sample.csv', mode ='r') as file:
 
#   c_File = csv.reader(file)

#   for lines in c_File:
#         print(lines)

from colorama import Cursor
import pandas as pd
import mysql.connector as msql
from mysql.connector import Error


empData = pd.read_csv('us-500.csv', index_col=False, delimiter = ',')
empData.head()

try:
    connection = msql.connect(host = 'localhost', user = 'root', password = '')
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE employeeData")
        print("Database is created")


except Error as e:
    print("Error while connecting to MySQL", e)