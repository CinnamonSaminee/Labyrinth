#-------------------------------------------------------------------------------
# Name:        labyrinth
# Purpose:  A program that prints a given maze file, finds the start location,
#           determines if the maze is solvable, and  prints the solution if
#           applicable.
# Author:      Samin Saberi
#
# Created:     02/06/2015
# Copyright:   (c) Samin 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Represents the maze stored in a 2-dimensional list for use by all functions
mazeList2d = []

#Function to load the file and store into global variable mazeList2d
#Parameter: filename
def loadMaze(themaze):
    #File is opened, each line is stored as a string in a list ('mazeList')
    mazeList = open(themaze,'r').readlines()

    #The global variable will be modified to store the maze
    global mazeList2d

    #Each character of every line is seperated and stored
    #in mazeList2d (without '\n')
    for line in mazeList[0:len(mazeList)-1]:
        mazeList2d += [list(line[0:-1])]
    #Extra '#' is accounted for on last line
    mazeList2d += [list(mazeList[-1])]


#Function to print the maze
def printMaze():
    #Each line is printed
    for line in mazeList2d[0:len(mazeList2d)]:
        for x in line:
            #'X' characters inserted by solve() are printed as ' '
            if x == "X":
                print(' ', end = '')
            else:
                print(x, end = '')
        print('')


#Function to find the starting coordinates of the maze, represented by 'S'
def findStart():
    xcoor = 0
    ycoor = 0

    #Loop iterates through mazeList2d until 'S' is found
    for y in mazeList2d[0:len(mazeList2d)]:
        xcoor = 0
        for x in y:
            if x == 'S':
                #coordinates stored in tuple
                spoint = (xcoor, ycoor)
            elif not x == 'S':
                xcoor += 1
        ycoor += 1

    return spoint


#Function to solve the maze
#Parameters: x and y coordinates of 'S'
#**Note: solve() can only be used once per maze to return a boolean value.
def solve(x,y):
    #The global variable will be modified
    global mazeList2d

    #Checks if there is a ' ' or 'E' on every direction
    #Left
    if mazeList2d[y][x-1] == ' ':
        #The spot is marked by an arrow
        mazeList2d[y][x-1] = '<'
        #Checks recursively if 'E' may be found in the current direction
        if solve(x-1,y):
            return True
        #Otherwise, the arrow is replaced with 'X' so the spot will
        #not be revisited
        elif not solve(x-1,y):
            mazeList2d[y][x-1] = 'X'
    #Base case of finding 'E' returns True
    elif mazeList2d[y][x-1] == 'E':
        return True

    #Process above is repeated for each direction
    #Right
    if mazeList2d[y][x+1] == ' ':
        mazeList2d[y][x+1] = '>'
        if solve(x+1,y):
            return True
        elif not solve(x+1,y):
            mazeList2d[y][x+1] = 'X'
    elif mazeList2d[y][x+1] == 'E':
        return True

    #Up
    if mazeList2d[y-1][x] == ' ':
        mazeList2d[y-1][x] = '^'
        if solve(x,y-1):
            return True
        elif not solve(x,y-1):
            mazeList2d[y-1][x] = 'X'
    elif mazeList2d[y-1][x] == 'E':
        return True

    #Down
    if mazeList2d[y+1][x] == ' ':
        mazeList2d[y+1][x] = 'v'
        if solve(x,y+1):
            return True
        elif not solve(x,y+1):
            mazeList2d[y+1][x] = 'X'
    elif mazeList2d[y+1][x] == 'E':
        return True

    #If there are no spaces to be checked, False is returned
    return False


def main():
    pass

    #Maze file is loaded
    loadMaze('sample.maze')
    #Empty maze is printed
    printMaze()
    #Start coordinates are found and printed
    print("Start Coordinates: ", findStart())
    #Solution is determined
    solvable = solve(findStart()[0],findStart()[1])
    #If a solution exists, it will be printed
    print("Solvable: ", solvable)
    if solvable:
        printMaze()


if __name__ == '__main__':
    main()
