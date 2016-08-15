#!/usr/bin/python3
import sys
import csv
import os.path

print("MC Package Manager")
if len(sys.argv) > 1 and len(sys.argv) < 5:



	if sys.argv[1] == "install":
		#iterating through mod list
		print("Installing...")
		if os.path.isfile("pkglist.csv") == True:
			pass
		else:
			print("Package list not found. Do something")
		#load csv
		with open('pkglist.csv') as packagelist:
			data = csv.DictReader(packagelist, delimiter=',')
			for row in data:
				#print(row['pkg'], row['version'], row['link'])
				if sys.argv[2] in row['pkg']:
					print("Package found!")
				else:
					#useless.
					print("Not found.")
					#pass


	elif sys.argv[1] == "update":
		#look for changes in the package list
		print("Updating...")
		if os.path.isfile("pkglist.csv") == True:
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

