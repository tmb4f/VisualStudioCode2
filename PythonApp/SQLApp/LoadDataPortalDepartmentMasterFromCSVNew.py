import numpy as np
import pandas as pd
import csv as csv
import pyodbc

dnamein = "C:\\Users\\tmb4f\\source\\Workspaces\\Tom Burgan - My Files\\Development\\GitRepositories\\BalancedScorecard\\Excel Documents"

fnamein = "departments.csv"

fi = open(dnamein + "\\" + fnamein)

#
# Read txt and store in dataframe.
#

csvreader = csv.reader(fi, delimiter=',', quotechar='"')

# This skips the first row of the CSV file.  Assuming there is a column header row.

next(csvreader)

# Create ODBC connection to target database

connStr = pyodbc.connect('DRIVER={SQL Server};SERVER=HSTSARTDMT;DATABASE=DS_HSDM_App_Dev;Trusted_Connection=yes')
cursor = connStr.cursor()

# Extract column names for target table and place in a list.
# (Assumes target table exists)

cursor.execute("SELECT TOP 1 * FROM Rptg.Data_Portal_Department_Master")

cursor_list = []

cursor_list = list(cursor.description)

cursor_array = np.array(cursor_list)

column_list = cursor_array[:,0].tolist()

cursor_list = None
cursor_array = None

# Truncate target tab le

cursor.execute("DELETE FROM Rptg.Data_Portal_Department_Master")

connStr.commit()
    
# Create dataframe
    
df = pd.DataFrame(columns = column_list)

# Load data into dataframe

for row in csvreader:
    df = df.append(dict(zip(column_list,row)),ignore_index=True)

# print(df)

df = df.fillna('')

# Create a string representing the list of columns that will inserted into the target table

column_string = '[' + '],['.join([f'{item}' for item in column_list]) + ']'

# Create a string containing the SQL statement arguments for the values that will be inserted into the target table

value_string = ','.join(['?' for item in column_list])

# print(column_string)
# print(value_string)

# for index,row in df.iterrows():
# 	data_list = row.tolist()
# 	print(','.join(data_list))

# Create SQL statement, defining the list of columns and their values/value arguments

query = f"INSERT INTO Rptg.Data_Portal_Department_Master({column_string}) VALUES ({value_string})"

# print(query)

"""was not returning a list of "list[s], tuple[s], or [pyodbc] Row[s]", it was returning a list of "numpy.records". The solution was to convert the "records" so that params contained a list of tuples:

params = list(tuple(row) for row in data_table.head(10).values)
"""

# Create a sequence composed of the parameters and their values, aligning to the arguments
params = list(tuple(row) for row in df.values)

# print(params)

# Generate SQL statment

cursor.executemany(query,params)

# Execute SQL statement

connStr.commit()

cursor.close()
connStr.close()

fi.close

df = None