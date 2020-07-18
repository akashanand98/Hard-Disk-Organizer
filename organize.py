import os
from os import path
from pathlib import Path

#  Hard disk Organizer #

def categorizeIn(value):
    if os.path.isdir(value) !=True:
        os.mkdir(value)   
    dirName=Path(value)    
    return dirName   
        

def categorize():
    extras=['.','-','[',']','(',')','{','}']
    langs=["tamil","malayalam","telugu","english","hindi","kannada"]
    for item in os.listdir():
        if os.path.isdir(item):
            continue
        else:
            filePath=Path(item)
            fileString=""
            for i in item:
                if i not in extras:
                    fileString=fileString+str(i)
                else:
                    fileString=fileString+ " "
            for x in fileString.split(' '):
                if str(x.lower()) in langs:
                    val=str(x.lower())
                    dirPath=categorizeIn(val)
                    filePath.rename(dirPath.joinpath(filePath))
                    break
                    
                    
        
# RUN the file on the directory in which you need to organize movies #       
categorize()        
