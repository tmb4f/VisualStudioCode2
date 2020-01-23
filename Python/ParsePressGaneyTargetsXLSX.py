#
# Extracts monthly ranks from .pdf document received from Press Ganey
#

import numpy as np
import pandas as pd

from tabula import read_pdf

dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\Data\\Goals"
dnameout = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\Data\\Goals\\Cleaned"

fnamein = "FY20 SL Targets.xlsx"
fnameout = "FY20 SL Targets New.txt"

fo = open(dnameout + "\\" + fnameout,'wb')

#
# Read xlsx and store in OrderedDict collection.  Each sheet name becomes the key value for the respective dataframe.
#

df = pd.io.excel.read_excel(dnamein + "\\" + fnamein, sheet_name=None)

# df.keys()
# df['CH-CAHPS'].head()
# for k, v in df.items():
#     print(k, v)

# print(df)

#
# Variables used to store relevant row ids and parsed text
#
  
domain_i = -1
domain_n = ""
daterange_i = -1
daterange_start = ""
daterange_end = ""
topbox_i = -1
columns = ['StartDate','EndDate','Question','Percentile','Rank']
dfo = pd.DataFrame(columns = columns)

#
# Iterate through dataframe by row
#
  
for i,row in df.iterrows():
 if row[0] == "All PG Database": # Page header row
     domain_i = i + 3 # Dataframe row with question name
     daterange_i = i + 1 # Dataframe row with date range
     topbox_i = i + 7 # First dataframe row with rank data
 if i == domain_i : domain_n = row[0] # Save question name
 if i == daterange_i: daterange_li = row[0].split(' - '); daterange_start = daterange_li[0]; daterange_end = daterange_li[1] # Save date range
 if i >= topbox_i: # Dataframe row contains rank data
     topbox_li = row[0].split() # Transform rank data row into a list
     for index, item in enumerate(topbox_li):
         if index % 2 == 0: # List item is a percentile
             nextitem = topbox_li[index+1] # Save rank for percentile
             dfo = dfo.append(dict(zip(columns, (daterange_start, daterange_end, domain_n, item, nextitem))),ignore_index=True)

# print(dfo)

array = dfo.values
df = None
np.savetxt(fo, array, fmt='%s', delimiter=",")
fo.close
dfo = None
array = None