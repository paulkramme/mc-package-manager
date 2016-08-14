#!/usr/bin/python3
import sys

print("MC Package Manager\n")
if len(sys.argv) == 1:
	print("Insufficient args\n")
	exit()
elif len(sys.argv) == 2:
	pass
else:
	print("Too much args\n")
