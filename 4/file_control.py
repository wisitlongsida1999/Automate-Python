# Ref : https://youtu.be/xTXGdKiY-NE

import os 
import shutil

print("This path is "+os.getcwd())
print("This dir is",os.listdir())

abs_path=os.getcwd()+'\excel\\'
print(abs_path)

dir_excel=os.listdir(abs_path)
print(dir_excel)

os.mkdir(os.getcwd()+'\\new excel')
new_abs_path=os.getcwd()+'\\new excel'
print(new_abs_path)

for file in dir_excel:
    shutil.move(abs_path+file,new_abs_path)

print("------------------Succesfull !!!!!")