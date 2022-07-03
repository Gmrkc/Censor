import glob
import os
import shutil

def remove(path, ext):
    removing_item = glob.glob('{path}*.{ext}'.format(path=path, ext=ext))
    for i in removing_item:
        os.remove(i)

def move(files, path):
    for file in files:
        new_path = path + file
        shutil.move(file, new_path)