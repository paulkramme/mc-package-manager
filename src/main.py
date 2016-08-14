#!/usr/bin/python3
import sys

print("MC Package Manager")
if len(sys.argv) > 1 and len(sys.argv) < 5:
	if sys.argv[1] == "install":
		#iterating through mod list
		print("Installing...")
	elif sys.argv[1] == "update":
		#look for changes in the package list
		print("Updating...")
	elif sys.argv[1] == "upgrade":
		#upgrade installed mods
		print("Upgrading...")
	else:
		print("No command found.")
