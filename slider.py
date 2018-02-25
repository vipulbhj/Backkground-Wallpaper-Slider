#!/usr/bin/python3

from os import listdir, system
from time import sleep

# The path of directory where all the images are stored.
PATH = r'/home/vipul/Desktop/Stuff/slider/'

# Getting the files that are available in the target folder.
allFiles = listdir(PATH)
# print(allFiles)

# We need to find out how many images are there in the folder , so that we can create a condition that
# will change the background for all the images.

size = len(allFiles)

# This flag variable is used to keep track of which image is current used as the wallpaper.
i = 0

# An infinite loop that keep the program going forever till it is executed.
while True:
    # Command required
    # gsettings set org.gnome.desktop.background picture-uri file:///path/to/the/file
    file = PATH + allFiles[i]
    command = r'gsettings set org.gnome.desktop.background picture-uri file:' + str(file)
    system(command)
    sleep(60)
    i += 1
    if i > size - 1:
        i = 0




#/home/vipul/Desktop/Stuff/slider/one.jpg
