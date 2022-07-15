import pandas as pd
student_names = ['Jennifer','John','Margaret','Jack','Jillian','Adam','Ali','Chris','Dylan','Kennedy']
out_of_state = [True,False,False,True,False,False,True,True,True,False]
table1 = pd.DataFrame(list(zip(student_names, out_of_state)), columns=["Student","Status"])
print(table1)
#
# Use 
for i,row in table1.iterrows(): # Converts each dataframe row to a series named "row"
    table1_li = row.tolist() # Transform series to a list object
    if table1_li[1] == True: print(table1_li[0]) # Use list indexing to select list values
for i,row in table1.iterrows():
    if row.Status == True: print(row.Student) # Use series indexing to select series values