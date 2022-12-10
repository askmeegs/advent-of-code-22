"""
the value of xreg controls the middle value of a sprite, 3 pixels wide.

xXx 

the CRT is 40 pixels wide, 6 high 
draws left to right, then the next row - like reading a book. 

6 rows 
each row numbered 0-39 

CRT draws 1 pixel per cycle

lit by sprite = # 
dark = . 

the sprite cares about me, +1, -1  -- because it's 3 pixels wide.

Task is to render the image of the CRT. In the small.txt, it's noise. 
But for input.txt, Eight capital letters should appear. what are they?
"""

def main(): 
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    instr = [line.split() for line in lines]


    # a 2D grid, 40 rows and 6 columns 
    grid = [['.' for i in range(40)] for j in range(6)]
    # pretty print the 2d grid

    cyclenum = 1
    xreg = 1 


    # every 1 cycle, draw 1 pixel 
    for i, item in enumerate(instr):
        if len(item) == 1: # noop 
            grid = draw(grid, xreg, cyclenum)
            cyclenum += 1
        else: # addx 
            grid = draw(grid, xreg, cyclenum)
            cyclenum += 1 
            grid = draw(grid, xreg, cyclenum)
            xreg += int(item[1]) 
            cyclenum += 1 
    print("🏁 DONE")
    printgrid(grid)

"""
every cycle has a draw function. 
the cyclenum tells us where we are in the grid.
"""
def draw(grid, xreg, cyclenum): 
    cyclenum -= 1
    # where are in the grid? 
    i = cyclenum // 40
    j = cyclenum % 40 
    print("\ncyclenum is {}, i={}, j={}".format(cyclenum, i, j))
    # where is the sprite? 🧚🏼
    sprite = [xreg-1, xreg, xreg+1]
    # is this pixel lit? 
    if j in sprite and j < 40:
        grid[i][j] = '#'
    printgrid(grid)
    return grid

def printgrid(grid):
    for row in grid:
        print(''.join(row))
    print("\n")


# execute main
if __name__ == '__main__':
    main()