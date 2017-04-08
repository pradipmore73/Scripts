#!/usr/bin/python
#  Author  : PRADIP MORE
#  Purpose : Using Functions,Lists to check for File Named babe ,if already exists append dude ,else create file 
import os

files = [f for f in os.listdir('/home/')]
capture = os.popen("ls | grep -i babe | tr -d '\n'").read()
print "Searching for babe in /home/"

def search(capture):
        for item in files:
                if capture in item:
                       return True
                return False

def create_file(capture):
                print "Creating babe..."
                os.popen("touch babe")
                print "<<<  Created  >>>"

def append_file(capture):
                print "Appending dude to babe"
                os.popen("echo dude >> babe")
                print "<<<  Appended  >>>"
                
if search(capture) :
        create_file(capture)
else:
        append_file(capture)
