import pandas as pd
student_names = ['Jennifer','John','Margaret','Jack','Jillian','Adam','Ali','Chris','Dylan','Kennedy']
out_of_state = [True,False,False,True,False,False,True,True,True,False]
table1 = pd.DataFrame(list(zip(student_names, out_of_state)), columns=["Student","Status"])
print(table1)
for i,row in table1.iterrows():
    table1_li = row.tolist() # Transform table1 data row into a list
    if table1_li[1] == True: print(table1_li[0])