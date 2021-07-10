#Ref = https://www.youtube.com/watch?v=h2dcAbxzKhI

import pandas as pd 

reader = pd.read_excel("Book1.xlsx").set_index("No.")
print(reader)
writer=pd.ExcelWriter("report.xlsx")
reader.to_excel(writer,"report1")
writer.save()

