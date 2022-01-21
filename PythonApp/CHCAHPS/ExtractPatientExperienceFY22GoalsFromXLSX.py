#
# Extracts FY targets from .xlsx document created by QPI Operational Anslytic/Patient Experience Office
#

import numpy as np
import pandas as pd

dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\Data\\Goals"
dnameout = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\Data\\Goals\\Cleaned"

# fnamein = "FY20 SL Targets.xlsx"
# fnameout = "FY20 SL Targets Staging.txt"
# fnamein = "PXO FY21 GoalSetting_5182020 (BC 7-13-20).xlsx"
# fnameout = "PXO FY21 GoalSetting_5182020 (BC 7-13-20) Staging.txt"
# fnamein = "FY22 Revised Goal Setting_12-7-2021.xlsx"
# fnameout = "FY22 Revised Goal Setting_12-7-2021 Staging.txt"
# fnamein = "FY22 Revised Goal Setting_12-28-2021.xlsx"
# fnameout = "FY22 Revised Goal Setting_12-28-2021 Staging.txt"
# fnamein = "FY22 Revised Goal Setting_1062022.xlsx"
# fnameout = "FY22 Revised Goal Setting_1062022 Staging.txt"
# fnamein = "FY22 Revised Goal Setting_1102022_1112022.xlsx"
# fnameout = "FY22 Revised Goal Setting_1102022_1112022 Staging.txt"
# fnamein = "FY22 Revised Goal Setting_(Tom)1132022_1132022.xlsx"
# fnameout = "FY22 Revised Goal Setting_(Tom)1132022_1132022 Staging.txt"
fnamein = "FY22 Revised Goal Setting_(Tom)1192022_1212022.xlsx"
fnameout = "FY22 Revised Goal Setting_(Tom)1192022_1212022 Staging.txt"


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

    # df=df.replace({';':''}, regex=True)

    # Set the index to become the last column
    df_to_print.set_index(df_to_print.columns[-1], inplace=True)
    # Add current index as a column, add new sequential index
    df_to_print.reset_index(inplace=True)
    
    # Create column headings list
    columns = []
    number_of_columns = len(df_to_print.columns)
    # columns = np.arange(1, number_of_columns, 1)
    columns = np.arange(0, number_of_columns, 1)
    
    dfo = None
    
    array = None
    
    row_index = -1
    # row_index = 0 # Defines previous row number for valid data row (i.e. skipping column header rows)

    # Loop through dataframe rows, appending relevant rows
    if len(df_to_print.columns) > 4: # Number of columns in sheet
        dfo = pd.DataFrame(columns = columns) # Define output datafame for appending relevant data rows
        for i,row in df_to_print.iterrows(): # For each row in sheet
            # # if row[5] == "Domain/Question":
            # #     dfo = pd.DataFrame(columns = columns)
            # #     row_index = i
            # if row[2] == "x":
            #     row_index = i
            row_index = i
            # # if row_index > -1 and i > row_index and not pd.isnull(row[5]):
            # # if row_index > 0 and i > row_index and not pd.isnull(row[2]):
            # if row[2] != "x" and row_index > -1 and i > row_index and not pd.isnull(row[2]):
            #     dfo = dfo.append(dict(zip(columns,pd.to_numeric(row.tolist(), errors='ignore'))),ignore_index=True)
            if row_index > -1:
                dfo = dfo.append(dict(zip(columns,pd.to_numeric(row.tolist(), errors='ignore'))),ignore_index=True)
               
    if row_index > -1:             
    # if row_index > 0:
        dfo = dfo.replace(np.nan,'', regex=True)

        # dfo=dfo.replace({',':''}, regex=True, inplace=True)

        # dfo = dfo.round(1)
        # dfo = dfo.astype('str')
        array = dfo.values

        # x = np.char.replace(array, ',', '')

        # fmt='"%s"'
        # np.savetxt(fo, array, fmt='%s', delimiter=",", encoding='utf-8')
        # np.savetxt(fo, x, fmt='%s', delimiter=",", encoding='utf-8')
        np.savetxt(fo, array, fmt='"%s"', delimiter=",", encoding='utf-8')

    dfo = None
    array = None
    x = None
    df_to_print = None
    
fo.close