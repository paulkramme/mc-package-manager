#!/usr/bin/python3
import sys
import json
import os.path
#from pprint import pprint

print("MC Package Manager")
if len(sys.argv) > 1 and len(sys.argv) < 5:
	if sys.argv[1] == "install":
		#iterating through mod list
		print("Installing...")
		if os.path.isfile("pkglist.json") == True:
			pass
		else:
			print("Package list not found. Run diggedigdi update.")

		with open("pkglist.json") as packagelist:
			jsondata = json.load(packagelist)
			#pprint(jsondata)

	elif sys.argv[1] == "update":
		#look for changes in the package list
		print("Updating...")
		if os.path.isfile("pkglist.json") == True:
			pass
		else:
			#download package list...
			print("Package list not found. Downloading...")
			#blabla
				
	elif sys.argv[1] == "upgrade":
		#upgrade installed mods
		print("Upgrading...")
	else:
		print("No command found.")
