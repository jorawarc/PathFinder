# PathFinder
Calculates a path between two non-negative integers by adding two specified integers and square rooting.

# Why was this developed
Path Finder was originally  created as a tool to solve this [riddle,](https://www.youtube.com/watch?v=YeMVoJKn1Tg) but has been generalized.
Riddle TL:DW
Starting from 0, get the numbers 2, 10, 14 by adding 5 or 7 and square rooting.
You are not allowed to:
 - Use the same number twice
 - Use decimal numbers
 - Have a current sum above 60
You can have as many numbers in between 2,10,14 so long as they do not violate the rules above

# What Path Finder Does
Path Finder accepts any two non-negative starting numbers and will calculate a path between them using two specified non-negative integers and square rooting.

Ex. One possible path between 0 and 2 by only using 5,7 and square rooting is `[0, 5, 10, 15, 22, 29, 36, 6, 11, 16, 4, 2]`

# How to use
`python .\pathfinder.py {starting number} {ending number} {addition number} {addition number}`

Ex. `python .\pathfinder.py 0 2 5 7`

# Constraints
 - All numbers must be non-negative
 
 # Final Note
 Path Finder calculates a path by recursively adding numbers, which is a memory intensive task.
 A `SOFT_MAX` has been put in place to avoid consuming too much memory but can be modified.
