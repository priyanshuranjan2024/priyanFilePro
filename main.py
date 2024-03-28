
import os
import shutil

path="C:\\Users\\KIIT0001\\Downloads"
files=os.listdir(path)
for file in files:
    fileName,extention=os.path.splitext(file)
    extention=extention[1:]
    if os.path.exists(path+"/"+extention):
        shutil.move(path+"/"+file,path+"/"+extention+"/"+file)  
    else:
        os.makedirs(path+"/"+extention)
        shutil.move(path+"/"+file,path+"/"+extention+"/"+file)

