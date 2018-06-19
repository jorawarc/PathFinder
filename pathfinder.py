# pathfinder.py
# Finds a path from a to b
# Rules:
# Only allowed to add X or Y starting from a
# Can Square root perfect square (no decimals)
# Author: Jorawar Chana

import sys
import math as m

# Globals 
order = []
seen = []

# Making this larger will slow down computation
# But increase the upper bound of testing
SOFT_MAX = 1000

# Brute force the lower bound
def minimizePath(num, sol, addX, addY):
    global order
    global seen

    # Log Variables
    # Used to check if prioritizing one addition value
    # reduces the path to the other
    i = 1
    k = 1

    prioritizeX = []
    merged = []

    # Find the lower bound while prioritizing X
    # Returns the lower bound
    print("Prioritizing " + str(addX) + "...")
    i = runner(num, sol, addX, addY)
    prioritizeX = order

    seen.clear()
    order.clear()
    
    # Find the lower bound while prioritizing Y
    print("Prioritizing " + str(addY) + "...")
    k = runner(num, sol, addY, addX)

    order.reverse()


    if i == SOFT_MAX:
        print("SOFT_MAX Reached")
        return -1
    elif k > i:
        order = prioritizeX
        return i-1
    elif k == i and order != prioritizeX:
        merged.append(order)
        merged.append(prioritizeX)
        order = merged
    return k-1

# Helper function to minimize path
def runner(num, sol, addX, addY):
    i = 0
    global seen
    while len(order) == 0 and i < SOFT_MAX:
        i += 1
        path(num,sol,addX,addY,i)
        seen.clear()
        if (i/200).is_integer():
            print("Trial: " + str(i))
    return i



# Find a path from num to sol
def path(num, sol, addX, addY, upperBound):

    if num in seen or num >= upperBound:
        return
    
    if num == sol:
        order.append(num)
        seen.append(num)
        return

    seen.append(num)
    
    # Assume that you always want to root a perfect square before adding X or Y
    if (m.sqrt(num).is_integer() and num != 0):
        numSquared = int(m.sqrt(num))
        path(numSquared, sol, addX, addY, upperBound)
    
    else:
        path(num+addX, sol, addX, addY, upperBound)
        path(num+addY, sol, addX, addY, upperBound)
    
    if len(order) == 0:
        return
    elif sol in order:
        if(order[-1] - num == addX or  order[-1] - num == addY) or order[-1] == int(m.sqrt(num)):
            order.append(num)



# [Starting Number] [Solution Number] [Addition X] [Addition Y]
def main():

    try:
        init = int(sys.argv[1])
        solution = int(sys.argv[2])
        additionX = int(sys.argv[3])
        additionY = int(sys.argv[4])

        bound = minimizePath(init,solution,additionX,additionY)
        if bound != -1:
            print("Minimum Bound: " + str(bound))
            print(order)
        else:
            print("No path found")
    except:
        print("Arguments Malformed")


# Execute
main()