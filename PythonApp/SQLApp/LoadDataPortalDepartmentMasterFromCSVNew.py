import numpy as np
import pandas as pd
import csv as csv
import pyodbc

""" Service_Dictionary = {'HCAHPS (2)': ['HCAHPS'],
'CH-CAHPS': ['CHCAHPS'],
'CG-CAHPS': ['CGCAHPS'],
'ED': ['ED']} """

dnamein = "C:\\Users\\tmb4f\\source\\Workspaces\\Tom Burgan - My Files\\Development\\GitRepositories\\BalancedScorecard\\Excel Documents"

fnamein = "departments.csv"

fi = open(dnamein + "\\" + fnamein)

#
# Read txt and store in dataframe.
#

csvreader = csv.reader(fi, delimiter=',', quotechar='"')

# This skips the first row of the CSV file.

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

cursor.commit()
    
# Create dataframe
    
df = pd.DataFrame(columns = column_list)

# Load data into dataframe

for row in csvreader:
    df = df.append(dict(zip(column_list,row)),ignore_index=True)

# print(df)

df = df.fillna('')

""" result= ''
    for element in list:
        result += str(element)"""

# def column_string(lst):
# 	string = ''
# 	for item in lst:
# 		string += '[' + str(item) + '],'
# 	return string
	
def column_string(lst, prefx, separator, sufx):
	# s = '],['
	return prefx + separator.join(lst) + sufx

def value_string(lst):
	# vlst = ['?' for item in lst]
	return ','.join(['?' for item in lst])

print(column_string(column_list,'[','],[',']'))
# print(column_string(column_list,"row['","'],row['","]"))
print(value_string(column_list))

for index,row in df.iterrows():
	data_list = row.tolist()
	print(','.join(data_list))

"""#
# Iterate through dataframe by row
#
  
for i,row in df.iterrows():
	csv_li = row.tolist() # Transform master location data row into a list

	for index, item in enumerate(csv_li):
		if index == 0: key = csv_li[index]
		if index == 1: level = csv_li[index]
		if index == 2: hsArea_sid = csv_li[index]
		if index == 3: sid = csv_li[index]
		if index == 4: display = csv_li[index]
		if index == 5: name_external = csv_li[index]
		if index == 6: name = csv_li[index]
		if index == 7: service_line_id = csv_li[index]
		if index == 8: service_line_type = csv_li[index]
		if index == 9: sub_service_line_id = csv_li[index]
		if index == 10: pod_id = csv_li[index]
		if index == 11: hub_id = csv_li[index]
		if index == 12: practice_group_id = csv_li[index]
		if index == 13: practice_id = csv_li[index]
		if index == 14: group_id = csv_li[index]
		if index == 15: department_id = csv_li[index]
		if index == 16: financial_division_id = csv_li[index]
		if index == 17: rev_location_id = csv_li[index]
		if index == 18: is_upg = csv_li[index]
		if index == 19: mc_som_id = csv_li[index]
		if index == 20: outpatient_flu = csv_li[index]
		if index == 21: ambulatory_scorecard = csv_li[index]
	
	dfo = dfo.append(dict(zip(csv_columns, (key,level,hsArea_sid,sid,display,name_external,name,service_line_id,service_line_type,sub_service_line_id,pod_id,hub_id,practice_group_id,practice_id,group_id,department_id,financial_division_id,rev_location_id,is_upg,mc_som_id,outpatient_flu,ambulatory_scorecard))),ignore_index=True)

dfo = dfo.fillna('')

# print(dfo)

for index,row in dfo.iterrows():
	cursor.execute("INSERT INTO Rptg.Data_Portal_Department_Master([key],[level],[hsArea_sid],[sid],[display],[name_external],[name],[service_line_id],[service_line_type],[sub_service_line_id],[pod_id],[hub_id],[practice_group_id],[practice_id],[group_id],[department_id],[financial_division_id],[rev_location_id],[is_upg],[mc_som_id],[outpatient_flu],[ambulatory_scorecard]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row['key'],row['level'],row['hsArea_sid'],row['sid'],row['display'],row['name_external'],row['name'],row['service_line_id'],row['service_line_type'],row['sub_service_line_id'],row['pod_id'],row['hub_id'],row['practice_group_id'],row['practice_id'],row['group_id'],row['department_id'],row['financial_division_id'],row['rev_location_id'],row['is_upg'],row['mc_som_id'],row['outpatient_flu'],row['ambulatory_scorecard'])
	connStr.commit()

cursor.close()
connStr.close()

fi.close()
df = None
dfs = None
dfo = None

dfo_unpivot = pd.melt(dfo.replace('null',np.nan),
   id_vars=['Service','Epic_Department_Id','Epic_Department_Name','Service_Line','Unit_Location','Domain_Question'],
   value_vars=dfo.columns.drop(['Service','Epic_Department_Id','Epic_Department_Name','Service_Line','Unit_Location','Domain_Question']).tolist(),
   value_name='Score') \
   .dropna() \
   .sort_values(['Service','Epic_Department_Id','Epic_Department_Name','Service_Line','Unit_Location','Domain_Question'])
   
dfo_unpivot['Score'] = dfo_unpivot['Score'].apply(lambda x: str(round(float(x),1)) if len(x) > 0 else x)

array = dfo_unpivot.values
df = None
dfo = None
dfo_unpivot = None
np.savetxt(fo, array, fmt='%s', delimiter=",")
array = None

fo.close() """