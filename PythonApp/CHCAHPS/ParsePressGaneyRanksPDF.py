#
# Extracts monthly ranks from .pdf document received from Press Ganey
#

import numpy as np
import pandas as pd

from tabula import read_pdf

#dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\071218"
#dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\081518"
#dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\091718"
#dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\101718"
#dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\111218"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\122118"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\011719"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\021819"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\031819"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\041619"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\051619"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\061719"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\071819"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\081519"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\091619"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\102219"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\111819"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\121819"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\011720"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\021420"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\031920"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\041520"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\051420"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\061720"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\071320"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\081720"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\091820"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\101920"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\111620"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\121520"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\012521"
# dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\021921"
dnamein = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Original From Client\\032221"
dnameout = "O:\\Computing Services\\INFSUP_S\\Documentation\\Projects\\Patient Experience\\CHCAHPS\\Data\\Percentile Rank\\Cleaned"

#fnamein = "2018_07 CHCAHPS TB_R - All PG Database_CMS View.pdf"
#fnameout = "2018_07 CHCAHPS TB_R - All PG Database_CMS View.txt"
#fnamein = "2018_08 CHCAHPS TB_R - All PG Database_CMS View.pdf"
#fnameout = "2018_08 CHCAHPS TB_R - All PG Database_CMS View.txt"
#fnamein = "2018_09 CHCAHPS TB_R - All PG Database_CMS View.pdf"
#fnameout = "2018_09 CHCAHPS TB_R - All PG Database_CMS View.txt"
#fnamein = "2018_10 CHCAHPS TB_R - All PG Database_CMS View.pdf"
#fnameout = "2018_10 CHCAHPS TB_R - All PG Database_CMS View.txt"
#fnamein = "2018_11 CHCAHPS TB_R - All PG Database_CMS View.pdf"
#fnameout = "2018_11 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2018_12 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2018_12 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2019_01 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2019_01 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2019_02 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2019_02 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2019_03 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2019_03 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2019_04 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2019_04 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2019_05 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2019_05 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2019_06 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2019_06 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2019_07 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2019_07 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2019_08 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2019_08 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2019_09 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2019_09 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2019_10 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2019_10 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2019_11 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2019_11 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2019_12 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2019_12 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2020_01 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2020_01 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2020_02 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2020_02 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2020_03 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2020_03 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2020_04 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2020_04 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2020_05 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2020_05 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2020_06 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2020_06 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2020_07 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2020_07 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2020_08 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2020_08 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2020_09 CHCAHPS TB_R - All PG Database.pdf"
# fnameout = "2020_09 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2020_10 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2020_10 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2020_11 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2020_11 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2020_12 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2020_12 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2021_01 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2021_01 CHCAHPS TB_R - All PG Database_CMS View.txt"
# fnamein = "2021_02 CHCAHPS TB_R - All PG Database_CMS View.pdf"
# fnameout = "2021_02 CHCAHPS TB_R - All PG Database_CMS View.txt"
fnamein = "2021_03 CHCAHPS TB_R - All PG Database.pdf"
fnameout = "2021_03 CHCAHPS TB_R - All PG Database_CMS View.txt"

fo = open(dnameout + "\\" + fnameout,'wb')

#
# Read pdf and store in dataframe.  Each row in pdf is placed in one dataframe column with no indexes.
#

df = read_pdf(dnamein + "\\" + fnamein, pages="all", guess=False, stream=True, pandas_options={'header':None})

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