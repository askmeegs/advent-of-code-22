"""
Sand fills a cave problem.

Example input:
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9

Each line represents a rock formation. (down, right)


  4     5  5
  9     0  0
  4     0  3
0 ......+...
1 ..........
2 ..........
3 ..........
4 ....#...##
5 ....#...#.
6 ..###...#.
7 ........#.
8 ........#.
9 #########.

The input determines the boundaries of the cave. (Grid) 
Everything around that is (Good Place Janet Voice) a boundless void. 

Once you have the rock formations populated (. = air, # = rock) SAND WILL BEGIN TO FALL. 
Sand falls one grain of sand at a time, filling one cell at a time. 

Sand starts at a "source" indicated with +  - the source is always (500,0)

SAND GRAVITY BEHAVIOR:
    - Default is, go straight down 1 step. 
    - If you can't, go 1 step down and to the left
    - If you can't, go 1 step down and to the right 
    - If you can't make any of those 3 moves, SAND COMES TO A STOP IN THE CURRENT AIR CELL, replace . with o (o = sand grain)


The task is to simulate as many sand grains as possible, UNTIL one grain of sand enters the void. 
The void is defined as falling below the lowest row of the cave. (max val of Y)
Return the # of grains of sand that came to a rest. 

Solution to small is: 24 
"""
import os 
def main(): 
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]


    # first, determine the grid boundaries. 
    # scan for minX, maxX, minY, maxY
    minX = 1000
    maxX = 0
    minY = 1000
    maxY = 0

    for line in lines: 
        # split line into 2 parts 
        pairs = line.split(' -> ')
        for p in pairs:
            y, x = p.split(',')
            x = int(x)
            y = int(y)
            if x < minX: 
                minX = x
            if x > maxX: 
                maxX = x
            if y < minY: 
                minY = y
            if y > maxY: 
                maxY = y

    # swap x and y
    print(minX, maxX, minY, maxY)
    # return
    numCols = maxY - minY +1 
    numRows = maxX +1 

    # draw the grid by starting with all air (".")
    grid = [['.' for i in range(numCols)] for j in range(numRows)]
    pretty(grid)
    # os.exit(0)
    # pretty(grid)
    # iterate over lines
    for line in lines:
        pairs = line.split(' -> ')
        for i in range(len(pairs)-1):
            p1 = pairs[i]
            p2 = pairs[i+1]
            y1, x1 = p1.split(',')
            y2, x2 = p2.split(',')
            x1 = int(x1)
            y1 = int(y1)
            x2 = int(x2)
            y2 = int(y2)
            # print("Drawing # line between: {},{} and {}, {}".format(x1, y1, x2, y2))
            
            # left to right
            # y needs to be adjusted
            if x1 == x2 and y1 < y2:
                for y in range(y1, y2+1):
                    # print("Attempting to draw at: {}, {}".format(x1, y-minY))
                    grid[x1][y-minY] = '#' 
            # right to left
            elif x1 == x2 and y1 > y2:
                for y in range(y2, y1+1):
                    # print("Attempting to draw at: {}, {}".format(x1, y-minY))
                    grid[x1][y-minY] = '#' 
            # top to bottom
            elif y1 == y2 and x1 < x2:
                for x in range(x1, x2+1):
                    # print("Attempting to draw at: {}, {}".format(x, y1-minY))
                    grid[x][y1-minY] = '#'
            # bottom to top
            else:
                for x in range(x2, x1+1):
                    # print("Attempting to draw at: {}, {}".format(x, y1-minY))
                    grid[x][y1-minY] = '#'
    pretty(grid)

    # it's that time, it'S SAND TIME 
    sandCount = 1

    x = 0 
    y = 500-minY
    print("Starting at: {}, {}".format(x, y))
    while True: 
        print("Sand grain #{}, coordinates: {}, {}".format(sandCount, x, y))
        # pretty(grid)
        # look down 
        if grid[x+1][y] == ".":
            x += 1 
            continue 
        # look down-left
        elif grid[x+1][y-1] == ".":
            x += 1 
            y -= 1 
            continue
        # look down right
        elif grid[x+1][y+1] == ".":
            x += 1 
            y += 1 
            continue
        # otherwise, STAY and increment sandCount by 1, RESET and try another grain 
        else:
            grid[x][y] = "o"
            if x == 0 and y == 500-minY:
                break
            sandCount += 1
            x = 0 
            y = 500-minY

    print("⏳ DONE!")
    print(sandCount)
    pretty(grid)

def pretty(grid):
    for row in grid:
        print(''.join(row))

# execute main
if __name__ == '__main__':
    main()
