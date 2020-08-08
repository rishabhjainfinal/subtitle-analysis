from module import most_common 
import os

# reading 
# module (name,fies,dir)
# two ways to do this


# first

# most_common('money heist S01',
# ['1.txt'
# ,'2.txt'
# ,'3.txt'
# ,'4.txt'
# ,'5.txt'
# ,'6.txt'
# ,'7.txt'
# ,'8.txt'
# ,'9.txt'
# ,'10.txt'
# ,'11.txt'
# ,'12.txt'
# ,'13.txt'],
# 'subtitles')


# second by specying directory 
# direc ='subtitles'
# most_common('money heist S01',os.listdir(direc),direc)


# if you wanna list many word from different file then just add files with dir and put last variable ='' 

def multiplefiles(folder_list):    
    file_path=[]
    for folder_name in folder_list:
        for i in os.listdir(folder_name):
            file_path.append(os.path.join(folder_name,i))
    most_common('all given files',file_path,'')


multiplefiles(['subtitles','subtitles1'])