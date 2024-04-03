# Mainipulates video data, prints output to screen
# Joshua Hofmann
# 4/02/2024

import math
import os
from video import *
import csv
import re

video_data_array = [] #used to store all data read from CSD file
read_row = 0

def read_video_data(row, line_num):
    global read_row
    col_num = 0

    #if line num increases, create new video data obj
    if (read_row != line_num):
        read_row = read_row + 1
        col_num = 0;
        video_data_array.append(video_data())

    current_video_data = video_data_array[-1] #returns last element CHAT GPT TAUGHT ME THIS

    for col in row:
        match col_num:
            case 0:
                current_video_data.link = col;
            case 1:
                current_video_data.title = col;
            case 2:
                current_video_data.view_count = int(col);
            case 3:
                current_video_data.likes_count =int(col);
            case 4:
                current_video_data.comments_count = int(col);
            case 5:
                current_video_data.published_date = col;
            case 6:
                #calculate duration
                duration_list = re.split(":", col)
                duration = int(duration_list[0]) * 60 + int(duration_list[1])
                current_video_data.duration = duration; #in seconds
            case 7:
                pass
            case 8:
                current_video_data.author = col;
            case _: 
                print("Col not Implmented update case statement to support")
        col_num = col_num + 1
    

#Step 1 read data from spread sheet, load objs
with open('input_data.csv') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        read_video_data(row, reader.line_num)
       
csv_file.close()

#Step 2 Work on data 



#Step 3 print data to screen for debug
for video_data in video_data_array:
    print(vars(video_data))

#Step 4 print to file


