#!/usr/bin/env python
import random

min_value = 1
# max_value = 6 this will be detemined by the starting statement
roll = "yes"


roll_numbers = raw_input("Please enter number of dice with number of sides (separate multiple with spaces) ie:\n3d6 2d20 4d8\n")

# Error - didn't give me the 'd'

string = roll_numbers.split()
for i, result in enumerate(string):
	string[i] = string[i].split("d")
	# print string
print string

# roll_again = "yes"
while roll == "yes" or roll == "y":
    print "Rolling the dice..."
    print "The values are...."
    for result in string:

		for i in range(0, int( result[0] ) ):
			print random.randint( min_value, int( result[1] ) )

    roll_again = raw_input("Re-roll? ")