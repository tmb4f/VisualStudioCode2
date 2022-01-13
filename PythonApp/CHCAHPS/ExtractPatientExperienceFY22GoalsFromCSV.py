import numpy as np
import pandas as pd
import csv as csv

# Service_Dictionary = {'HCAHPS': ['HCAHPS'],
# 'CH-CAHPS': ['CHCAHPS'],
# 'CGCAHPS': ['CGCAHPS'],
# 'ER': ['ED']}

Service_Line_Dictionary = {'Inpatient': ['HCAHPS'],
'Inpatient Pediatrics': ['CHCAHPS'],
'OP Clinics': ['CGCAHPS'],
'Emergency Department': ['ED']}

dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\Data\\Goals\\Cleaned"
dnameout = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\Data\\Goals\\Cleaned"

# fnamein = "PXO FY21 GoalSetting_5182020 (BC 7-13-20) Staging.txt"
# fnameout = "FY21 SL Targets.txt"

# fnamein = "FY22 Revised Goal Setting_12-7-2021 Staging.txt"
# fnamein = "FY22 Revised Goal Setting_12-28-2021 Staging.txt"
# fnamein = "FY22 Revised Goal Setting_1062022 Staging.txt"
# fnamein = "FY22 Revised Goal Setting_1102022_1112022 Staging.txt"
fnamein = "FY22 Revised Goal Setting_(Tom)1132022_1132022 Staging.txt"

fnameout = "FY22 SL Targets.txt"

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

# dfs = df.iloc[:,[1,2,3,4,6,7,8,18,21]]

dfs = df.iloc[:,[1,2,3,4,5,6,7,8,9,10,11,12,13]]

# service_columns = ['Service','Reporting_Level','Domain','Question','Epic_Department_Id','Epic_Department_Name','Service_Line','FY2021_Unit_Score','FY2021_All_SL_Score']

service_line_columns = ['Service_Line','Epic_Department_Id','Epic_Department_Name','Domain','Question','FY2022_Unit_Score','Organization','FY2022_Organization_Score','Service','FY2022_Service_Score','Clinical_Area','FY2022_Clinical_Area_Score','FY2022_All_SL_Score']

# service_line_columns = ['Service_Line','Epic_Department_Id','Epic_Department_Name','Domain','Question','FY2022_Unit_Score','Clinical_Area','FY2022_Clinical_Area_Score','Service','FY2022_Service_Score','Organization','FY2022_Organization_Score','FY2022_All_SL_Score']

# dfo = pd.DataFrame(columns = service_columns)

dfo = pd.DataFrame(columns = service_line_columns)

#
# Iterate through dataframe by row
#
  
for i,row in dfs.iterrows():
	topbox_li = row.tolist() # Transform goal data row into a list
	
	# if row[2] in Service_Dictionary.keys():
	
	if row[2] in Service_Line_Dictionary.keys():

		for index, item in enumerate(topbox_li):        
			# if index == 0: Service = Service_Dictionary[topbox_li[index]][0]        
			if index == 0: Service_Line = Service_Line_Dictionary[topbox_li[index]][0]
			if index == 1: Epic_Department_Id = str(int(float(topbox_li[index]))) if len(topbox_li[index]) > 0 else topbox_li[index]
			if index == 2: Epic_Department_Name = topbox_li[index]
			if index == 3: Domain = topbox_li[index]
			if index == 4: Question = topbox_li[index]
			if index == 5: FY2022_Unit_Score = topbox_li[index]
			# if index == 6: Organization = topbox_li[index]
			# if index == 7: FY2022_Organization_Score = topbox_li[index]
			# if index == 8: Service = topbox_li[index]
			# if index == 9: FY2022_Service_Score = topbox_li[index]
			# if index == 10: Clinical_Area = topbox_li[index]
			# if index == 11: FY2022_Clinical_Area_Score = topbox_li[index]
			# if index == 12: FY2022_All_SL_Score = topbox_li[index]
			if index == 10: Organization = topbox_li[index]
			if index == 11: FY2022_Organization_Score = topbox_li[index]
			if index == 8: Service = topbox_li[index]
			if index == 9: FY2022_Service_Score = topbox_li[index]
			if index == 6: Clinical_Area = topbox_li[index]
			if index == 7: FY2022_Clinical_Area_Score = topbox_li[index]
			if index == 12: FY2022_All_SL_Score = topbox_li[index]
	
		# dfo = dfo.append(dict(zip(service_columns, (Service,Reporting_Level,Domain,Question,Epic_Department_Id,Epic_Department_Name,Service_Line,FY2021_Unit_Score,FY2021_All_SL_Score))),ignore_index=True)
	
		dfo = dfo.append(dict(zip(service_line_columns, (Service_Line,Epic_Department_Id,Epic_Department_Name,Domain,Question,FY2022_Unit_Score,Organization,FY2022_Organization_Score,Service,FY2022_Service_Score,Clinical_Area,FY2022_Clinical_Area_Score,FY2022_All_SL_Score))),ignore_index=True)

dfo = dfo.fillna('')
dfo.rename(index=str, columns={"FY2022_Unit_Score": "2022"}, inplace=True)

dfo_unpivot_1 = pd.melt(dfo.replace('null',np.nan),
   # id_vars=['Service','Reporting_Level','Epic_Department_Id','Epic_Department_Name','Service_Line','Domain','Question','FY2021_All_SL_Score'],
   id_vars=['Service_Line','Epic_Department_Id','Epic_Department_Name','Domain','Question','Organization','FY2022_Organization_Score','Service','FY2022_Service_Score','Clinical_Area','FY2022_Clinical_Area_Score','FY2022_All_SL_Score'],
   # value_vars=dfo.columns.drop(['Service','Reporting_Level','Epic_Department_Id','Epic_Department_Name','Service_Line','Domain','Question','FY2021_All_SL_Score']).tolist(),
   value_vars=dfo.columns.drop(['Service_Line','Epic_Department_Id','Epic_Department_Name','Domain','Question','Organization','FY2022_Organization_Score','Service','FY2022_Service_Score','Clinical_Area','FY2022_Clinical_Area_Score','FY2022_All_SL_Score']).tolist(),
   value_name='Unit_Score',
   var_name='FY') \
   .dropna() \
   .sort_values(['Service_Line','Epic_Department_Id','Epic_Department_Name','Domain','Question','Organization','FY2022_Organization_Score','Service','FY2022_Service_Score','Clinical_Area','FY2022_Clinical_Area_Score','FY2022_All_SL_Score'])
   # .sort_values(['Service','Reporting_Level','Epic_Department_Id','Epic_Department_Name','Service_Line','Domain','Question','FY2021_All_SL_Score'])
    
dfo_unpivot_1.drop(['FY'], axis = 1, inplace = True) 
dfo_unpivot_1['Unit_Score'] = dfo_unpivot_1['Unit_Score'].apply(lambda x: str(round(float(x),1)) if len(x) > 0 else x)

# dfo_unpivot_1.rename(index=str, columns={"FY2021_All_SL_Score": "2021"}, inplace=True)
dfo_unpivot_1.rename(index=str, columns={"FY2022_All_SL_Score": "SL_Score"}, inplace=True)

dfo_unpivot_1.rename(index=str, columns={"FY2022_Organization_Score": "Organization_Score"}, inplace=True)
dfo_unpivot_1.rename(index=str, columns={"FY2022_Service_Score": "Service_Score"}, inplace=True)
dfo_unpivot_1.rename(index=str, columns={"FY2022_Clinical_Area_Score": "Clinical_Area_Score"}, inplace=True)

dfo_unpivot_2 = pd.melt(dfo_unpivot_1.replace('null',np.nan),
   id_vars=['Service_Line','Epic_Department_Id','Epic_Department_Name','Domain','Question','Organization','Organization_Score','Service','Service_Score','Clinical_Area','Clinical_Area_Score','Unit_Score'],
   value_vars=dfo_unpivot_1.columns.drop(['Service_Line','Epic_Department_Id','Epic_Department_Name','Domain','Question','Organization','Organization_Score','Service','Service_Score','Clinical_Area','Clinical_Area_Score','Unit_Score']).tolist(),
   value_name='All_SL_Score',
   var_name='FY') \
   .dropna() \
   .sort_values(['Service_Line','Epic_Department_Id','Epic_Department_Name','Domain','Question','Organization','Organization_Score','Service','Service_Score','Clinical_Area','Clinical_Area_Score','Unit_Score'])
    
dfo_unpivot_2.drop(['FY'], axis = 1, inplace = True)
dfo_unpivot_2['All_SL_Score'] = dfo_unpivot_2['All_SL_Score'].apply(lambda x: str(round(float(x),1)) if len(x) > 0 else x)
 
dfo_unpivot_2['Organization_Score'] = dfo_unpivot_2['Organization_Score'].apply(lambda x: str(round(float(x),1)) if len(x) > 0 else x) 
dfo_unpivot_2['Service_Score'] = dfo_unpivot_2['Service_Score'].apply(lambda x: str(round(float(x),1)) if len(x) > 0 else x) 
dfo_unpivot_2['Clinical_Area_Score'] = dfo_unpivot_2['Clinical_Area_Score'].apply(lambda x: str(round(float(x),1)) if len(x) > 0 else x)

array = dfo_unpivot_2.values
df = None
dfo = None
dfo_unpivot_1 = None
dfo_unpivot_2 = None
# np.savetxt(fo, array, fmt='%s', delimiter=",")
np.savetxt(fo, array, fmt='"%s"', delimiter=",")
array = None

fo.close()