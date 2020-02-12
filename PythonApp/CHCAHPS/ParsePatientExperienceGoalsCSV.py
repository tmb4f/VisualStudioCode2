import numpy as np
import pandas as pd

from tabula import read_pdf
from pandas import read_csv

dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Goals\\Provided by Patient Experience\\110518"
# dnameout = "F:\\Visual Studio 2017\\Projects\\Python\\CHCAHPS"
dnameout = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Goals\\Cleaned"

fnamein = "CHCAHPS PX Goal Setting As Of Jun (SL FINAL 20181012 V13).csv"
fnameout = "CHCAHPS PX Goal Setting As Of Jun (SL FINAL 20181012 V13).txt"

fo = open(dnameout + "\\" + fnameout,'wb')

#
# Read csv and store in dataframe.
#

df = read_csv(dnamein + "\\" + fnamein, skiprows=6)

#print(df)

df = df.fillna('')

##
## Variables used to store relevant row ids and parsed text
##

columns = ['Service_Line','Unit_Location','Domain_Question','FY2017_Score','FY2018_Score','FY2019_Score']
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
		if index == 0: Service_Line = topbox_li[index]
		if index == 1: Unit_Location = topbox_li[index]
		if index == 2: Domain_Question = topbox_li[index]
		# if index == 20: FY2017_Score = topbox_li[index]
		if index == 24: FY2017_Score = topbox_li[index]
		# if index == 28: FY2018_Score = topbox_li[index]
		if index == 35: FY2018_Score = topbox_li[index]
		if index == 47: FY2019_Score = topbox_li[index]
	
	dfo = dfo.append(dict(zip(columns, (Service_Line, Unit_Location, Domain_Question, FY2017_Score, FY2018_Score, FY2019_Score))),ignore_index=True)

# print(dfo)

dfo = dfo.fillna('')
dfo.rename(index=str, columns={"FY2017_Score": "2017", "FY2018_Score": "2018", "FY2019_Score": "2019"}, inplace=True)
# dfo.head()

dfo_unpivot = pd.melt(dfo.replace('null',np.nan),
   id_vars=['Service_Line','Unit_Location','Domain_Question'],
   value_vars=dfo.columns.drop(['Service_Line','Unit_Location','Domain_Question']).tolist(),
   value_name='Score') \
   .dropna() \
   .sort_values(['Service_Line','Unit_Location','Domain_Question'])

array = dfo_unpivot.values
# print(array)
df = None
dfo = None
np.savetxt(fo, array, fmt='%s', delimiter=",")
fo.close
dfo_unpivot = None
df = None
array = None