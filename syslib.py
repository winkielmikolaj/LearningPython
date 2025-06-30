import sys

#you have to start this program by terminal to work properly
try:
	print("Hello, my name is", sys.argv[1])
except IndexError:
	print("Too few arguments. Write your name or try to run this program by terminal")