#
# Extracts FY targets from .xlsx document created by Patient Experience Office
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

od = pd.io.excel.read_excel(dnamein + "\\" + fnamein, sheet_name=None)

Sheet_names_list = []

for sheet, df in od.items():
    Sheet_names_list.append(sheet)

# Sheet_names_list = ['EVS-Dietary']

for sheet in Sheet_names_list :
    df_to_print = od[sheet]
    df_to_print['Sheet_Name'] = sheet
    # Set the index to become the last column
    df_to_print.set_index(df_to_print.columns[-1], inplace=True)
    # Add current index as a column, add new sequential index
    df_to_print.reset_index(inplace=True)
    
    # Create column headings list
    columns = []
    number_of_columns = len(df_to_print.columns)
    columns = np.arange(1, number_of_columns, 1)
    
    dfo = None
    
    array = None
    
    row_index = -1

    # Loop through datafrane rows, appending relevant rows
    if len(df_to_print.columns) > 4: # 
        for i,row in df_to_print.iterrows():
            if row[5] == "Domain/Question":
                dfo = pd.DataFrame(columns = columns)
                row_index = i
            if row_index > -1 and i > row_index and not pd.isnull(row[5]):
                dfo = dfo.append(dict(zip(columns,pd.to_numeric(row.tolist(), errors='ignore'))),ignore_index=True)
               
    if row_index > -1:
        dfo = dfo.replace(np.nan,'', regex=True)
        # dfo = dfo.round(1)
        # dfo = dfo.astype('str')
        array = dfo.values
        np.savetxt(fo, array, fmt='%s', delimiter=",", encoding='utf-8')

    df_to_print = None
    
fo.close