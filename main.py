#firstly import all the required modules

import os
import shutil

import sys
import time
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_dir="C:\Users\KIIT0001\Downloads"#common for all my university student's laptop



class MoverHandler(FileSystemEventHandler):
    def on_modified(self,event):
        files=os.listdir(source_dir) #this will list all the directories the the source_dir

    #now use a for loop
        for file in files:
          fileName,extension=os.source_dir.splitext(file)
          extension=extension[1:]#removing the .

    #now doing the main work
          if os.source_dir.exists(source_dir+'/'+extension):
            shutil.move(source_dir+'/'+file,source_dir+'/'+extension+'/'+file)#it will move from source to destination
          else:
        #create the directory then move the file into that
            os.makedirs(source_dir+'/'+extension)
            shutil.move(source_dir+'/'+file,source_dir+'/'+extension+'/'+file)


       
    


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    source_dir = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, source_dir, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
