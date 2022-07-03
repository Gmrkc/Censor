import os
import time
import glob
import file_utils
import shutil
from yolov5 import detect
from yolov5 import detect2
from drivedemo import DriveDemo
import timeit

drive_demo = DriveDemo()
while True:

    #time.sleep(120)

    # 1RWd7Jhl5t1qRoWZv7S0wm25Dzbv9h5XO -> directory id of edited files
    # 1HqUkoNS2zyNIM-hREUZYuFtvBJK7nmIA -> directory id of raw files

    raw_files = "1RWd7Jhl5t1qRoWZv7S0wm25Dzbv9h5XO"
    edited_files = "1HqUkoNS2zyNIM-hREUZYuFtvBJK7nmIA"

    raw_file_list = drive_demo.get_file_list(raw_files)
    #print(raw_file_list)
    edited_file_list = drive_demo.get_file_list(edited_files)
    #difference_list = drive_demo.get_difference_lists(raw_file_list, edited_file_list)

    raw_file_list = drive_demo.get_only_title(raw_file_list)
    #print(raw_file_list)
    edited_file_list = drive_demo.get_only_title(edited_file_list)
    difference_list = drive_demo.get_difference_lists(raw_file_list, edited_file_list)

    #print(raw_file_list)
    #print(edited_file_list)
    #print(difference_list)
    if len(difference_list) == 0:
        continue

    drive_demo.download_files(raw_files, difference_list)
    file_utils.move(difference_list, "temp_files/")
    video_input = os.listdir('temp_files/')

    if len(video_input) > 0:
        detect.main('temp_files/')
        detect2.main('temp_files2/')
        print(difference_list)
        for name in difference_list:
            drive_demo.upload_file("{a}".format(a=name), edited_files)
            #start = timeit.default_timer()
            os.remove("temp_files/{b}".format(b=name))
            os.remove("temp_files2/{b}".format(b=name))
            #stop = timeit.default_timer()
            #print('Time: ', stop - start) 
    else: 
        pass

    main_files = os.listdir()

    for file in main_files:
        if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.mp4'):
            os.remove(file)
    