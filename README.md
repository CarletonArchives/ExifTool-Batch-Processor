# ExifTool-Batch-Processor
Code by Caitlin Donahue caitlindonahue95@gmail.com

This program will automatically run ExifTool on the folders contained within a directory supplied by the user.  A CSV report and an XML report of the ExifTool analysis will be placed in a subfolder of each processed bag titled /data/meta.

##ExifTool:
ExifTool is a program written by Phil Harvey to read and write the meta information contained in files.
ExifTool can be dowloaded here: http://www.sno.phy.queensu.ca/~phil/exiftool/
For this program you want to install the *Image-ExifTool distribution* (This should be the first Download button on the page)
Documentation for exiftool can be found here: http://www.sno.phy.queensu.ca/~phil/exiftool/exiftool_pod.html#reading_examples
Instructions for exiftool can be found here: https://wiki.carleton.edu/display/carl/Exif+Metadata+Extraction+Tool

###Preparing exiftool:
There is a little bit of preparation required for this pogram to work with Exifool properly.
####Windows:
On Windows you need to add exiftool to your path.
Basic instructions on installing exiftool can be found under the *Full Perl Distribution* section here:
http://owl.phy.queensu.ca/~phil/exiftool/install.html#Windows

1. Download *Image-ExifTool distribution* and unzip the file. 

2. Rename the file "exiftool" to "exiftool.pl"

3. in the directory C:\Windows create a directory called "exiftool"

4. in the files you downloaded, move the folder "lib" and the file "exiftool.pl" to C:\Windows\exiftool

5. if you are using Windows 8 go to the Control Panel->System->Advanced System Settings-> Environment Variables. If you are using an earlier version of windows go to My Computer->Properties->Advanced->Environmental Settings.

6. Locate the variable named PATH. Click to edit that variable and add C:\Windows\exiftool; to the end.

7. To check if these steps were successful go to the Command Prompt and type "exiftool.pl" and press enter. If successful an information message about exiftool should pop up.

8. You are now ready to run this program.

####Mac:
Basic instructions on installing exiftool on a mac can be found under the *Full Perl Distribution* section here:
http://owl.phy.queensu.ca/~phil/exiftool/install.html#OSX

1. Download *Image-ExifTool dstribution* The file should have a name like "Image-ExifTool-#.##.tar.gz", where #.## is the version number. in future steps, replace #.## with that number. Unzip the file to your Desktop.
2. Launch the terminal.
3. In the terminal enter the following lines:

                  cd ~/Desktop
                  tar -xzf Image-ExifTool-#.##.tar.gz
                  cd Image-ExifTool-#.##
                  sudo cp -r exiftool lib /usr/bin
4. you can check if these steps were successful by opening a new terminal window, and typing "exiftool" If the steps were successful a usage message should show up.


##Installing Perl:
Exiftool requires Perl version 5.004 or newer to be installed on your computer.
Instructions on installing Perl can be found here: http://learnperl.scratchcomputing.com/install/

##Installing Python:
You will need Python 2.7 installed on your computer to run this program.
Python can be found here: https://www.python.org/download/releases/2.7.5/


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
  - Running with no arguments will prompt you for the directory you would like to analyze.

- python RunExifTool.py <path to files to analyze>:
  - This will automatically run Exiftool on the directory you provide
  

###Input
- A directory of bags (folders) to run exiftool's analysis on.

###Output
- An .xml file containing exiftool's analysis in each bag.
- A .csv file containing exiftool's analysis in each bag.

###Example of syntax
If you would like to run exiftool using different options, use these samples to execute the program in Bach or a command prompt.

exiftool -csv -r /Users/nwilson/Desktop/20120430_3_publicationsphotos_2001 > /Users/nwilson/Desktop/20120430_3_publicationsphotos_2001/meta/metadata.csv

Writes a csv file of all tagged metadata, recursively going through all of Users/nwilson/Desktop/20120430_3_publicationsphotos_2001 and writing that information to /Users/nwilson/Desktop/20120430_3_publicationsphotos_2001/meta/metadata.csv
exiftool -X /Volumes/ARCHIVES/SIPS/1-unprocessed/20120605_HonorsCompsTheater2012/THE_TEMPEST_10_27_2011.mp4 > /Users/nwilson/Desktop/metadata.xml 

Writes an XML file of all tagged metadata non-recursively for THE_TEMPEST_10_27_2011.mp4 and writes the results to metadata.xml.
exiftool -r -X /Volumes/ARCHIVES/SIPS/11-Bagit/20120429_NoonNewsBulletinSamples1996 > /Volumes/ARCHIVES/SIPS/11-Bagit/20120429_NoonNewsBulletinSamples1996/meta/exif.xml

Writes and XML file of all tagged metadata recursively for 20120429_NoonNewsBulletinSamples1996 and writes the result to a new xml file in /Volumes/ARCHIVES/SIPS/11-Bagit/20120429_NoonNewsBulletinSamples1996/meta/exif.xml
exiftool -r -X /Volumes/ARCHIVES/SIPS/11-Bagit/20120429_NoonNewsBulletinSamples1996 > /Volumes/ARCHIVES/SIPS/11-Bagit/20120429_NoonNewsBulletinSamples1996/meta/exif.xml ; exiftool -X /Volumes/ARCHIVES/SIPS/1-unprocessed/20120605_HonorsCompsTheater2012/THE_TEMPEST_10_27_2011.mp4 > /Users/nwilson/Desktop/metadata.xml

Writes an XML file first for all files in the 20120429_NoonNewsBulletinSamples1996 directory, and then an XML file for THE_TEMPEST_10_27_2011.mp4.  The ";" separator allows you to run a series of commands.  For more information on different conditions you can apply see: http://www.comptechdoc.org/os/linux/manual2/runningcommands.html
