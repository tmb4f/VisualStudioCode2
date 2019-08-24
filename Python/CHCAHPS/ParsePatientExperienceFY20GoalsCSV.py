import numpy as np
import pandas as pd

from tabula import read_pdf
from pandas import read_csv

dnamein_CHCAHPS = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Goals\\Provided by Patient Experience\\082319"
dnamein_CGCAHPS = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CGCAHPS\\Data\\Goals\\FY2020"
dnamein_HCAHPS = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\HCAHPS\\Data\\Goals\\Provided by Patient Experience\\082319"
dnamein_ED = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\ED\\Data\\Goals\\FY2020"
# dnameout = "F:\\Visual Studio 2017\\Projects\\Python\\CHCAHPS"
dnameout = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\Data\\Goals\\Cleaned"

fnamein_CHCAHPS = "FY20 SL Targets CHCAHPS.csv"
fnamein_CGCAHPS = "FY20 SL Targets CGCAHPS.csv"
fnamein_HCAHPS = "FY20 SL Targets HCAHPS.csv"
fnamein_ED = "FY20 SL Targets ED.csv"
fnameout = "FY20 SL Targets.txt"

fo = open(dnameout + "\\" + fnameout,'ab')

#
# Read csv and store in dataframe - CHCAHPS.
#

Service = 'CHCAHPS'

df = read_csv(dnamein_CHCAHPS + "\\" + fnamein_CHCAHPS, usecols = [0, 1, 2, 3, 4, 45], skiprows=6, dtype=str)

df = df.fillna('')

# df['EPIC DEPT ID'] = df['EPIC DEPT ID'].astype(str)

# print(df)
# print(df['EPIC DEPT ID'].dtypes)

# df.columns.tolist()

#
# Variables used to store relevant row ids and parsed text
#

columns = ['Service','Epic_Department_Id','Epic_Department_Name','Service_Line','Unit_Location','Domain_Question','FY2020_Score']
# columns = ['GOAL_YR','SERVICE_LINE','UNIT','DOMAIN','GOAL']

dfo = pd.DataFrame(columns = columns)

#
# Iterate through dataframe by row
#
  
for i,row in df.iterrows():
	topbox_li = row.tolist() # Transform goal data row into a list
	#numEl = len(topbox_li)
	#print(i, topbox_li)
	#print(numEl)

	for index, item in enumerate(topbox_li):
		#print(i, index, item)
		if index == 0: Epic_Department_Id = topbox_li[index]
		if index == 1: Epic_Department_Name = topbox_li[index]
		if index == 2: Service_Line = topbox_li[index]
		if index == 3: Unit_Location = topbox_li[index]
		if index == 4: Domain_Question = topbox_li[index]
		if index == 5: FY2020_Score = topbox_li[index]
	
	dfo = dfo.append(dict(zip(columns, (Service,Epic_Department_Id,Epic_Department_Name,Service_Line, Unit_Location, Domain_Question, FY2020_Score))),ignore_index=True)

# print(dfo)

dfo = dfo.fillna('')
dfo.rename(index=str, columns={"FY2020_Score": "2020"}, inplace=True)
# dfo['Epic_Department_Id'].astype(str)
# dfo.head()
# print(dfo)

dfo_unpivot = pd.melt(dfo.replace('null',np.nan),
   id_vars=['Service','Epic_Department_Id','Epic_Department_Name','Service_Line','Unit_Location','Domain_Question'],
   value_vars=dfo.columns.drop(['Service','Epic_Department_Id','Epic_Department_Name','Service_Line','Unit_Location','Domain_Question']).tolist(),
   value_name='Score') \
   .dropna() \
   .sort_values(['Service','Epic_Department_Id','Epic_Department_Name','Service_Line','Unit_Location','Domain_Question'])

array = dfo_unpivot.values
# print(array)
df = None
dfo = None
dfo_unpivot = None
np.savetxt(fo, array, fmt='%s', delimiter=",")
array = None

#
# Read csv and store in dataframe - CGCAHPS.
#

Service = 'CGCAHPS'

df = read_csv(dnamein_CGCAHPS + "\\" + fnamein_CGCAHPS, usecols = [0, 1, 2, 3, 4, 45], skiprows=6, dtype=str)

#print(df)

df = df.fillna('')

##
## Variables used to store relevant row ids and parsed text
##

columns = ['Service','Epic_Department_Id','Epic_Department_Name','Service_Line','Unit_Location','Domain_Question','FY2020_Score']
#columns = ['GOAL_YR','SERVICE_LINE','UNIT','DOMAIN','GOAL']

dfo = pd.DataFrame(columns = columns)

#
# Iterate through dataframe by row
#
  
for i,row in df.iterrows():
	topbox_li = row.tolist() # Transform rank data row into a list
	#numEl = len(topbox_li)
	#print(i, topbox_li)
	#print(numEl)

	for index, item in enumerate(topbox_li):
		#print(i, index, item)
		if index == 0: Epic_Department_Id = topbox_li[index]
		if index == 1: Epic_Department_Name = topbox_li[index]
		if index == 2: Service_Line = topbox_li[index]
		if index == 3: Unit_Location = topbox_li[index]
		if index == 4: Domain_Question = topbox_li[index]
		if index == 5: FY2020_Score = topbox_li[index]
	
	dfo = dfo.append(dict(zip(columns, (Service,Epic_Department_Id,Epic_Department_Name,Service_Line, Unit_Location, Domain_Question, FY2020_Score))),ignore_index=True)

# print(dfo)

dfo = dfo.fillna('')
dfo.rename(index=str, columns={"FY2020_Score": "2020"}, inplace=True)
# dfo['Epic_Department_Id'].astype(str)
# dfo.head()

dfo_unpivot = pd.melt(dfo.replace('null',np.nan),
   id_vars=['Service','Epic_Department_Id','Epic_Department_Name','Service_Line','Unit_Location','Domain_Question'],
   value_vars=dfo.columns.drop(['Service','Epic_Department_Id','Epic_Department_Name','Service_Line','Unit_Location','Domain_Question']).tolist(),
   value_name='Score') \
   .dropna() \
   .sort_values(['Service','Epic_Department_Id','Epic_Department_Name','Service_Line','Unit_Location','Domain_Question'])

array = dfo_unpivot.values
# print(array)
df = None
dfo = None
dfo_unpivot = None
np.savetxt(fo, array, fmt='%s', delimiter=",")
array = None

#
# Read csv and store in dataframe - HCAHPS.
#

Service = 'HCAHPS'

df = read_csv(dnamein_HCAHPS + "\\" + fnamein_HCAHPS, usecols = [0, 1, 2, 3, 4, 45], skiprows=7, dtype=str)

#print(df)

df = df.fillna('')

##
## Variables used to store relevant row ids and parsed text
##

columns = ['Service','Epic_Department_Id','Epic_Department_Name','Service_Line','Unit_Location','Domain_Question','FY2020_Score']
#columns = ['GOAL_YR','SERVICE_LINE','UNIT','DOMAIN','GOAL']

dfo = pd.DataFrame(columns = columns)

#
# Iterate through dataframe by row
#
  
for i,row in df.iterrows():
	topbox_li = row.tolist() # Transform rank data row into a list
	#numEl = len(topbox_li)
	#print(i, topbox_li)
	#print(numEl)

	for index, item in enumerate(topbox_li):
		#print(i, index, item)
		if index == 0: Epic_Department_Id = topbox_li[index]
		if index == 1: Epic_Department_Name = topbox_li[index]
		if index == 2: Service_Line = topbox_li[index]
		if index == 3: Unit_Location = topbox_li[index]
		if index == 4: Domain_Question = topbox_li[index]
		if index == 5: FY2020_Score = topbox_li[index]
	
	dfo = dfo.append(dict(zip(columns, (Service,Epic_Department_Id,Epic_Department_Name,Service_Line, Unit_Location, Domain_Question, FY2020_Score))),ignore_index=True)

# print(dfo)

dfo = dfo.fillna('')
dfo.rename(index=str, columns={"FY2020_Score": "2020"}, inplace=True)
# dfo['Epic_Department_Id'].astype(str)
# dfo.head()

dfo_unpivot = pd.melt(dfo.replace('null',np.nan),
   id_vars=['Service','Epic_Department_Id','Epic_Department_Name','Service_Line','Unit_Location','Domain_Question'],
   value_vars=dfo.columns.drop(['Service','Epic_Department_Id','Epic_Department_Name','Service_Line','Unit_Location','Domain_Question']).tolist(),
   value_name='Score') \
   .dropna() \
   .sort_values(['Service','Epic_Department_Id','Epic_Department_Name','Service_Line','Unit_Location','Domain_Question'])

array = dfo_unpivot.values
# print(array)
df = None
dfo = None
dfo_unpivot = None
np.savetxt(fo, array, fmt='%s', delimiter=",")
array = None

#
# Read csv and store in dataframe - ED.
#

Service = 'ED'

df = read_csv(dnamein_ED + "\\" + fnamein_ED, usecols = [0, 1, 2, 3, 4, 45], skiprows=6, dtype=str)

#print(df)

df = df.fillna('')

##
## Variables used to store relevant row ids and parsed text
##

columns = ['Service','Epic_Department_Id','Epic_Department_Name','Service_Line','Unit_Location','Domain_Question','FY2020_Score']
#columns = ['GOAL_YR','SERVICE_LINE','UNIT','DOMAIN','GOAL']

dfo = pd.DataFrame(columns = columns)

#
# Iterate through dataframe by row
#
  
for i,row in df.iterrows():
	topbox_li = row.tolist() # Transform rank data row into a list
	#numEl = len(topbox_li)
	#print(i, topbox_li)
	#print(numEl)

	for index, item in enumerate(topbox_li):
		#print(i, index, item)
		if index == 0: Epic_Department_Id = topbox_li[index]
		if index == 1: Epic_Department_Name = topbox_li[index]
		if index == 2: Service_Line = topbox_li[index]
		if index == 3: Unit_Location = topbox_li[index]
		if index == 4: Domain_Question = topbox_li[index]
		if index == 5: FY2020_Score = topbox_li[index]
	
	dfo = dfo.append(dict(zip(columns, (Service,Epic_Department_Id,Epic_Department_Name,Service_Line, Unit_Location, Domain_Question, FY2020_Score))),ignore_index=True)

# print(dfo)

dfo = dfo.fillna('')
dfo.rename(index=str, columns={"FY2020_Score": "2020"}, inplace=True)
# dfo['Epic_Department_Id'].astype(str)
# dfo.head()

dfo_unpivot = pd.melt(dfo.replace('null',np.nan),
   id_vars=['Service','Epic_Department_Id','Epic_Department_Name','Service_Line','Unit_Location','Domain_Question'],
   value_vars=dfo.columns.drop(['Service','Epic_Department_Id','Epic_Department_Name','Service_Line','Unit_Location','Domain_Question']).tolist(),
   value_name='Score') \
   .dropna() \
   .sort_values(['Service','Epic_Department_Id','Epic_Department_Name','Service_Line','Unit_Location','Domain_Question'])

array = dfo_unpivot.values
# print(array)
df = None
dfo = None
dfo_unpivot = None
np.savetxt(fo, array, fmt='%s', delimiter=",")
array = None

fo.close