#firstly import all the required directory since 
#since i require to control the os
import os
import shutil

path=input("Enter the path:")
files=os.listdir(path) #this will list all the directories the the path

#now use a for loop
for file in files:
    fileName,extension=os.path.splitext(file)
    extension=extension[1:]#removing the .

    #now doing the main work
    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file,path+'/'+extension+'/'+file)#it will move from source to destination
    else:
        #create the directory then move the file into that
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
        