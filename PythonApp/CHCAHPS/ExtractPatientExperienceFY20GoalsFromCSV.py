import numpy as np
import pandas as pd
import csv as csv

Service_Dictionary = {'HCAHPS (2)': ['HCAHPS'],
'CH-CAHPS': ['CHCAHPS'],
'CG-CAHPS': ['CGCAHPS'],
'ED': ['ED']}

dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\Data\\Goals\\Cleaned"
dnameout = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\Data\\Goals\\Cleaned"

fnamein = "FY20 SL Targets New.txt"
fnameout = "FY20 SL Targets New New.txt"

fo = open(dnameout + "\\" + fnameout,'ab')
fi = open(dnamein + "\\" + fnamein)

#
# Read txt and store in dataframe.
#

csvreader = csv.reader(fi, delimiter=',', quotechar='"')
    
# Create column headings list
all_service_columns = np.arange(1, 100, 1)
    
df = pd.DataFrame(columns = all_service_columns)

for row in csvreader:
    df = df.append(dict(zip(all_service_columns,row)),ignore_index=True)

#
# Parse relevant data in dataframe
#

dfs = df.iloc[:,[0,1,2,3,4,5,46]]

service_columns = ['Service','Epic_Department_Id','Epic_Department_Name','Service_Line','Unit_Location','Domain_Question','FY2020_Score']

dfo = pd.DataFrame(columns = service_columns)

#
# Iterate through dataframe by row
#
  
for i,row in dfs.iterrows():
	topbox_li = row.tolist() # Transform goal data row into a list
	
	if row[1] in Service_Dictionary.keys():

		for index, item in enumerate(topbox_li):        
			if index == 0: Service = Service_Dictionary[topbox_li[index]][0]
			if index == 1: Epic_Department_Id = str(int(float(topbox_li[index]))) if len(topbox_li[index]) > 0 else topbox_li[index]
			if index == 2: Epic_Department_Name = topbox_li[index]
			if index == 3: Service_Line = topbox_li[index]
			if index == 4: Unit_Location = topbox_li[index]
			if index == 5: Domain_Question = topbox_li[index]
			if index == 6: FY2020_Score = topbox_li[index]
	
		dfo = dfo.append(dict(zip(service_columns, (Service,Epic_Department_Id,Epic_Department_Name,Service_Line, Unit_Location, Domain_Question, FY2020_Score))),ignore_index=True)

dfo = dfo.fillna('')
dfo.rename(index=str, columns={"FY2020_Score": "2020"}, inplace=True)

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

fo.close()