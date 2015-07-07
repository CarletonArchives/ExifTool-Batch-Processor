"""
RunExifTool is a program to automatically run exiftool on a set of bags contained within a directory supplied by the user
Dependencies:
-exif_settings.txt must be in the same directory as RunExifTool.py
-Must have exiftool installed on your computer
-Must have perl version 5.004 or newer n your computer

Code by Caitlin Donahue
caitlindonahue95@gmail.com
Summer 2015  
"""

import os
import sys
import platform
import ast
import errno

def usage_message():
    print "RunExifTool is a program to automatically run exiftool on a set of bags contained within a directory supplied by the user" 
    print "--------------------"
    print "Usage:"
    print "-h or --help to display this message"
    print "<python RunExifTool.py> with no arguments will prompt you for the required paths"
    print "<python RunExifTool.py <path to files to validate>> will check settings file for an existing path to exiftool, or prompt you for the path"
    print "<python RunExifTool.py <path to files to validate> <path to exiftool files>> will run the program, and save the exif path to the settings file"
    print "--------------------"
    print "Dependencies:"
    print "exif_settings.txt must be in the same directory as RunExifTool.py"
    print "Must have exiftool installed on your computer"
    print "Must have perl version 5.004 or newer n your computer"

def main():
    #store the original directory so we can navigate back to it at the end of the program
    original_location = os.getcwd()
    parent = ""
    exif = ""
    exifName = ""
    if len(sys.argv) == 2:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            usage_message()
        else:
            parent = sys.argv[1]
    if parent == "":
        #get file locations from the user
        print "Please enter the directory that holds the bags you would like to scan: "
        parent = raw_input().strip()

    #check what os the user is running to account for terminal command differences
    if platform.system() == "Windows":
        exifName = "exiftool.pl"
    else:
        exifName = "./exiftool"
    #make sure the directories are in the correct format
    parent = parent.strip().strip("'").strip('"')
    #navigate to the file that the user's exif program is located in     
    #make a list of all of the folders in this directory
    path_list = [x for x in os.listdir(parent)]

    for folder in path_list:
        full_folder_path = os.path.join(parent, folder).strip()
        if os.path.isdir(full_folder_path):
            print "--------------------------------------"
            print "Running exif tool on files in " + full_folder_path
            print "--------------------------------------"
            meta_path = os.path.join(full_folder_path,"data","meta")
            print "--------------------------------------"
            print "Making sure " + meta_path + " exists."
            print "--------------------------------------"
            try:
                os.makedirs(meta_path)
            #If an error is raised
            #ignore it if it is telling us the file already exists
            #raise the error if it is related to something else
            except OSError as exception:
                if exception.errno != errno.EEXIST:
                    raise
            full_folder_path = ('"' + full_folder_path + '"')
            meta_path = ('"' + meta_path + '"')
            print "--------------------------------------"
            print "Making xml file in " + meta_path
            print "--------------------------------------"
            cmd = exifName + " -r -X " + full_folder_path + " > " + os.path.join(meta_path, "exif.xml")
            os.system(cmd)
            print "--------------------------------------"
            print "Making csv file in " + meta_path
            print "--------------------------------------"
            cmd = exifName + " -csv -r " + full_folder_path + " > " + os.path.join(meta_path, "exif.csv")
            os.system(cmd)
            print "--------------------------------------"
            print "Run on " + full_folder_path + " complete"
            print "--------------------------------------"
    print "--------------------------------------"
    print "Run Complete"
    print "--------------------------------------"
main()