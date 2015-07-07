# ExifTool-Batch-Processor
Code by Caitlin Donahue caitlindonahue95@gmail.com

This program will automatically run exiftool on the folders contained within a directory supplied by the user.

Once you have run RunExifTool.py it will store the path to your exiftool files.

##ExifTool:
ExifTool is a program written by Phil Harvey to read and write the meta information contained in files.
ExifTool can be dowloaded here: http://www.sno.phy.queensu.ca/~phil/exiftool/
Documentation for exiftool can be found here: http://www.sno.phy.queensu.ca/~phil/exiftool/exiftool_pod.html#reading_examples
Instructions for exiftool can be found here: https://wiki.carleton.edu/display/carl/Exif+Metadata+Extraction+Tool
exiftool does not require any installation.

##Installing Perl:
Exiftool requires Perl version 5.004 or newer to be installed on your computer.
Instructions on installing Perl can be found here: http://learnperl.scratchcomputing.com/install/

##Installing Python:
You will need Python installed on your computer to run this program.
Python can be found here: https://www.python.org/download/releases/2.7.5/
or here: https://www.python.org/download/releases/3.2.2/

Instructions on setting up Pyton on your computer can be found here: https://apps.carleton.edu/curricular/cs/resources/source/python_install/


##Usage Instructions:
(Mac) Open a terminal window by navigating to "Applications -> Utilities -> Terminal" and clicking on the Terminal icon
(PC) Open a command prompt by selecting Start/Run and typing cmd and Enter or Start/Programs/Accessories/Command Prompt.

Navigate in your terminal to the folder in which RunExifTool.py is contained.

      cd PATH_TO_FOLDER_CONTAINING_EXIFTOOL

Once there there are several options on how to run the program.

- python RunExifTool.py (option)
  - Options are -h or --help 
  - This will display a usage message.

- python RunExifTool.py:
  - Running with no arguments will prompt you for the required paths.

- python RunExifTool.py <path to files to validate>:
  - If you have run the program before, or if you have added the location of your exiftool files to the exif_settings.txt file, this will automatically run.
  - If you have not already supplied the program with the location of your exiftool files, the program will prompt you for the path.
  - Upon prompting you for the path to the exiftool files, the program will save their location for future use.

- python RunExifTool.py <path to files to validate> <path to exiftool Files>:
  - This will run the program without needing to prompt the user for any paths
  - The supplied path to the exiftool files will be added to the settings file.

###Input
- A directory of bags (folders) to run exiftool's analysis on.

###Output
- An .xml file containing exiftool's analysis in each bag.
- A .csv file containing exiftool's analysis in each bag.

