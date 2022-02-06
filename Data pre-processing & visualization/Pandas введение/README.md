
```python
# import pandas as pd
import pandas as pd
  
  
# Create some Pandas dataframes from some data.
df1 = pd.DataFrame({'Data': [11, 12, 13, 14]})
df2 = pd.DataFrame({'Data': [21, 22, 23, 24]})
df3 = pd.DataFrame({'Data': [31, 32, 33, 34]})
df4 = pd.DataFrame({'Data': [41, 42, 43, 44]})
  
# Create a Pandas Excel writer object
# using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_positioning.xlsx', 
                             engine ='xlsxwriter')
  
# write and Positioning the dataframes in the worksheet.
# Default position, cell A1.
df1.to_excel(writer, sheet_name ='Sheet1')  
df2.to_excel(writer, sheet_name ='Sheet1', startcol = 3)
df3.to_excel(writer, sheet_name ='Sheet1', startrow = 6)
  
# It is also possible to write the
# dataframe without the header and index.
df4.to_excel(writer, sheet_name ='Sheet1',
             startrow = 7, startcol = 4,
             header = False, index = False)
  
# Close the Pandas Excel writer object
# and output the Excel file.
writer.save()
```
[](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-5319.png)
