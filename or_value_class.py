import pandas as pd
import openpyxl as px # to read and write excel files

file = 'unclassified_dnawise3.xlsx'
wb_obj = px.load_workbook(file)
sheet_obj = wb_obj.active # working in the active sheet

# maximum rows and columns values
rows = sheet_obj.max_row
columns = sheet_obj.max_column
print('Total rows:', rows)
print('Total columns:', columns)

#c2 = sheet_obj.cell(row = 2, column = 2)

# looping through each row in one column, and then writing out the classfied value in the next column
for i in range(2,rows + 1):
    cell_obj = sheet_obj.cell(row=i, column=1) 
    #print(cell_obj.value)
    value = cell_obj.value  #saving the value from this cell to the variable
    #c2 = sheet_obj.cell(row = 2, column = 2)
    #print(value)
    #value2 = float(value)
    #type(value2)
    #print(value2)

    #classifying, while converting 'string' to 'float'
    if((float(value)) >= 1.09):
        category = 'Increased risk'
    elif((float(value)) < 1):
        category = 'Decreased risk'
    elif((float(value))>=1 and (float(value)<1.1)):
        category = 'Typical risk'
    else:
        category = 'NA'
    
    #iterating the column 2 through each row and saving it in c2
    # while assigning the category value to each row in the column
    c2 = sheet_obj.cell(row = i, column = 2)
    c2.value = category
    
#saving and writing out the file    
wb_obj.save('dnawise3_classified.xlsx')



