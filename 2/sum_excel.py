#Ref = https://www.youtube.com/watch?v=Al_pjRo8wNE
import os
import pandas as pd 
import openpyxl


path = os.getcwd()+"/excel/"
print(path)
all_files=os.listdir(path)
print(all_files)
report=pd.DataFrame()
for file in all_files:
    print(file)
    reader=pd.read_excel(path+file).set_index("Product")
    print(reader)
    report=report.add(reader,fill_value=0)
print(report)
report["All Year"]=report.sum(axis=1)
report.loc["All Product"]=report.sum(axis=0)
print(report)
report.to_excel("Total Report.xlsx")
