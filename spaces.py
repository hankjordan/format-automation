import os, sys
#import argparse

#May be implemented in a future release
#parser = argparse.ArgumentParser()
#parser.parse_args()

if (len(sys.argv) < 3):
	print("Too few arguments!")
	print("")
	print("usage: spaces.py directory extension")
	print("spaces.py C:/programming/python/myproject py")
	sys.exit()

#Gets arguments for directory and extension
dir=sys.argv[1]	
ext=sys.argv[2]

#Verifies that the user has entered the correct directory
verify = input("The directory you chose is "+dir+", is this correct? (y/n): ")
if (verify != "y"):
	print("User exited program, quitting!")
	sys.exit()

#Verifies that the user has entered the correct extension
verify = input("The extension you chose is "+ext+", is this correct? (y/n): ")
if (verify != "y"):
	print("User exited program, quitting!")
	sys.exit()

#Checks if user supplied directory actually exists
if (not os.path.isdir(dir)):
	print("Directory invalid, quitting!")
	sys.exit()

#Define spaces and tabs
spaces = "    "
tab = "\t"

#Recursively moves through given directory
for root, dirs, files in os.walk(dir):
	for file in files:
		if (file.endswith("."+ext)):
			#If the file extension matches
			
			#Make the full path easier to use and look nice
			longfile = os.path.join(root, file).replace("\\","/")
			
			print("Modifying "+longfile)
			
			#Opens file for reading, reads it into a string, replaces the spaces with tabs
			fr = open(longfile,"r")
			text = fr.read().replace(spaces,tab)
			fr.close()
			
			#Opens the file for writing, writes the edited file in place
			fw = open(longfile,"w")
			fw.write(text)
			fw.close()