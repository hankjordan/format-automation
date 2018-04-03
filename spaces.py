import os, sys
import argparse

#Initializes argument parser to handle the arguments
parser = argparse.ArgumentParser(description="Recursively replaces spaces with tabs")

#Creates arguments for program
parser.add_argument("directory")
parser.add_argument("extension")
parser.add_argument("-q","--quiet",action="store_true",help="toggle quiet mode (no input/output or verification)")

#Shows help if no arguments are entered
if len(sys.argv)==1:
	parser.print_help(sys.stderr)
	sys.exit(1)

#Finalizes arguments and gets the results
args = parser.parse_args()

#Gets arguments for directory and extension
dir=args.directory
ext=args.extension

if (not args.quiet):
	#Verifies that the user has entered the correct directory
	verify = input("The directory you chose is "+dir+", is this correct? (y/n): ")
	if (verify != "y"):
		print("User exited program, quitting!")
		sys.exit(1)

	#Verifies that the user has entered the correct extension
	verify = input("The extension you chose is "+ext+", is this correct? (y/n): ")
	if (verify != "y"):
		print("User exited program, quitting!")
		sys.exit(1)

#Checks if user supplied directory actually exists
if (not os.path.isdir(dir)):
	print("Directory invalid, quitting!")
	sys.exit(1)

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
			
			if (not args.quiet):
				print("Modifying "+longfile)
			
			#Opens file for reading, reads it into a string, replaces the spaces with tabs
			fr = open(longfile,"r")
			text = fr.read().replace(spaces,tab)
			fr.close()
			
			#Opens the file for writing, writes the edited file in place
			fw = open(longfile,"w")
			fw.write(text)
			fw.close()