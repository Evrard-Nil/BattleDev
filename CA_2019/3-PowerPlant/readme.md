# Objective
You go down the snowy slopes on your super snowboard (listening to all the best remixes of 2003) while avoiding the trees to reach the bottom of the mountain at MetroCity. You can move to the right, left or downwards, but not up the track! The goal of this challenge is to determine the minimum number of moves you have to make to reach the bottom of the track. You can choose any starting point on the top of the track and arrive at any point at the bottom of the track.
# Data format
## Input
Row 1: two integers N and M between 2 and 1000 and separated by a space.
Rows 2 to N+1: a string of M characters representing the topology of the slope at a given altitude. A character X indicates the presence of a tree, a character . indicates snow.
## Output 
The minimum number of moves you need to make to reach the bottom of the slope (any cell with snow on the last row) from the top of the track (any cell with snow on the first row) without hitting a tree, or -1 if it’s not possible.
# Exemples
## Input
13 7
X..X...
X.X..XX
X.X....
.XXX.X.
X..X...
XXXX...
X.X..X.
X.X.XXX
.XX..XX
X.X....
X..X..X
X.X..X.
X.X..XX
## Output
14