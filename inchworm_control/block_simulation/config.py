from enum import Enum

# this file holds variables that the user can change just in this file before running

BD_LOC = [8, 1, 8]
CURRENT_LOC = [1, 0, 1]
# Define the possible orientations of the inchworm
InchwormOrientation = Enum('InchwormOrientaton', ['NORTH', 'SOUTH', 'EAST', 'WEST'])
CURRENT_ORIENTATION = InchwormOrientation.SOUTH