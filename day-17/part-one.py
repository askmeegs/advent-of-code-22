"""
Day 17 - "Pyroclastic Flow"  = Volcano bits 🌋

You're in a cave chamber. 5 types of rocks are falling: 

"horiz-bar"
####

"diamond
.#.
###
.#.

"tetris"
..#
..#
###

"vert-bar"
#
#
#
#

"square boy" 
##
##


The rocks fall in this order, 1-5, over and over again.
Jets of hot air come from the walls, and move the rocks L/R as they fall. 

>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>

The chamber is 7 feet wide. Rocks appear so that left edge is 2 ft away from 
the left wall. The bottom edge of the rock is 3 ft above the highest rock in the room, or the floor 

The pattern of falling is:
1. Appears
2. Goes 1ft L or R as indicated by pattern (repeat the pattern when run out)
3. Falls 1ft down  

If any L-R movement causes a rock to move into a wall, floor, or another rock, don't move. 
If moving D causes the rock to move into the floor or a rock, STOP. and go with the next rock. 

|.......|
|.......|
|.......|
|.......|
+-------+

This is the chamber, empty.  (7 ft wide and infinitely tall) 
Moving rocks are indicated with @ 
Stopped rocks indicated with #  

This is the simulation after 10 rocks. With the small.txt movement pattern

|.......|
|.......|
|.......|
|....#..|
|....#..|
|....##.|
|##..##.|
|######.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

With the small L/R pattern, 2022  


"""

def main(): 
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    line = lines[0] 
    pattern = ['R' if x == '>' else 'L' for x in line]

    """
    the chamber is represented by a list of lists. 
    from TOP (chamber[0]) TO BOTTOM 
    """

    # initialize the chamber with 5 empty rows 
    print("Initializing the empty chamber with height 0...")
    chamber = []
    prettyprint(chamber) 

    r_index = 0  # of rocks that have been placed, increments monotonically 
    r_looper = 0
    p_index = -1 # index within the pattern, which we loop through 

    # eventually this while loop will go up to 2023 
    while r_index < 1000000000000:
        # 1. rock appears 
        r_index += 1 
        print("🪨 On rock #{}".format(r_index))
        if r_looper == 5: 
            r_looper = 1
        else:
            r_looper += 1
        print("⭐️⭐️⭐️⭐️⭐️⭐️ New rock!! 🪨 Placing rock {} at the top ⭐️⭐️⭐️⭐️⭐️⭐️⭐️".format(r_index))
        if r_looper == 1:
            # horizontal bar 
            coords = [[0, 2], [0, 3], [0, 4], [0, 5]]
            chamber, coords = place_rock(chamber, coords, 1)
        if r_looper == 2: 
            # diamond 
            coords = [[0, 3], [1, 2], [1, 3], [1, 4], [2, 3]]
            chamber, coords = place_rock(chamber, coords, 2)
        if r_looper == 3:
            # reverse L 
            coords = [[0, 4], [1, 4], [2, 2], [2, 3], [2, 4]]
            chamber, coords = place_rock(chamber, coords, 3)
        if r_looper == 4:
            # vertical bar 
            coords = [[0, 2], [1, 2], [2,2], [3,2]]
            chamber, coords = place_rock(chamber, coords, 4)
        if r_looper == 5: 
            # 2x2 square 
            coords = [[0, 2], [0, 3], [1, 2], [1, 3]]
            chamber, coords = place_rock(chamber, coords, 5)
        prettyprint(chamber)

        # execute 2-3 until rock settles...  updated chamber and coords along the way
        # 2. rock moves L/R
        # 3. rock falls D
        while True:
            # increment pattern
            if p_index == len(pattern)-1:
                print("🚨 pattern is done! starting back at 0")
                p_index = 0
            else:
                p_index += 1
            # 2. IF IT CAN, rock moves L/R 
            if pattern[p_index] == 'L':
                # print("⬅️ Moving rock {} LEFT:".format(r_index))
                chamber, coords = move_left(chamber, coords)
                # prettyprint(chamber)
            else:
                # print("➡️ Moving rock {} RIGHT:".format(r_index))
                chamber, coords = move_right(chamber, coords)
                # prettyprint(chamber)
            # 3. move down. if it can't, BREAK and move to the next rock
            # print("⬇️ Moving rock {} DOWN:".format(r_index))
            chamber, coords, stuck = move_down(chamber, coords)
            if stuck: 
                # print("I'm stuck :(")
                chamber = freeze_rock(chamber, coords)
                chamber = chop_empty_rows(chamber)
                # prettyprint(chamber)
                break
    # we're done if we've placed X rocks. 
    # print the chamber height after that # of rocks.
    print("🏁 DONE - The height of the chamber after {} rocks is: {}".format(r_index, len(chamber)))


def chop_empty_rows(chamber):
    # chop empty rows off the top to ensure accurate height calculation 
    i = 0 
    pop = 0
    while i < len(chamber):
        if chamber[i] == ['.']*7:
            pop += 1 
            i += 1 
        else:
            break
    print("I need to pop {} rows.".format(pop))
    for _ in range(0, pop):
        chamber.pop(0)
    return chamber

def prettyprint(chamber): 
    # print rows from top to bottom
    for row in chamber: 
        print("|{}|".format("".join(row)))
    # print floor 
    print("+-------+")
    print("\n")
        

"""
Each rock appears so that its left edge is two units away 
from the left wall and its bottom edge is three units above 
the highest rock in the room (or the floor, if there isn't one).
"""


def place_rock(chamber, coords, rock_type): 
    # ignore 0 index, use 1-5 
    rock_heights = [0, 1, 3, 3, 4, 2] 

    for a in range(0, 3 + rock_heights[rock_type]):
        # add empty row to the front - beginning - of the list 
        chamber.insert(0, ['.']*7)
    # prettyprint(chamber) 
    # place the rock 
    for c in coords:
        chamber[c[0]][c[1]] = "@"

    return chamber, coords 


# given a rock with current coords [0, 2], [0, 3], [0, 4], [0, 5]
# ie. i=the row in the chamber, j = the col in the row 
# a rock is reprsented by a list of lists: the coordinates for all the @ bits 
# the length of that list is either 4 or 5, given the size of the rocks 
# if you hit a wall with ANY of the bits, DO NOT EXECUTE THE MOVE, simply return c as-is with the rock unmoving
def move_left(chamber, coords):
    # if we're about to move into another rock or the wall, do nothing
    for c in coords:
        if c[1] == 0:
            return chamber, coords
        if chamber[c[0]][c[1]-1] == "#":
            return chamber, coords
    # else, move left by first flipping the old coords to . 
    for i, c in enumerate(coords):
        chamber[c[0]][c[1]] = "."
    # now iterate on the coords and set all new bits to @ 
    for i, c in enumerate(coords):
        coords[i] = [c[0], c[1]-1]
        chamber[c[0]][c[1]-1] = "@"
    return chamber, coords

def move_right(chamber, coords):
    # if we're already against the right wall, or about to move into another rock, do nothing
    for c in coords:
        if c[1] == 6:
            return chamber, coords
        if chamber[c[0]][c[1]+1] == "#":
            return chamber, coords
    # else, move right by first flipping the old coords to . 
    for i, c in enumerate(coords):
        chamber[c[0]][c[1]] = "."
    # now iterate on the coords and set all new bits to @ 
    for i, c in enumerate(coords):
        coords[i] = [c[0], c[1]+1]
        chamber[c[0]][c[1]+1] = "@"
    return chamber, coords

# return True iff stuck 
def move_down(chamber, coords): 
    # check if we can move 
    for c in coords:
        if c[0] == len(chamber)-1:
            print("❌ Rock is stuck at the bottom! Done placing this rock.")
            return chamber, coords, True
        if chamber[c[0]+1][c[1]] == "#":
            print("⬇️ 🪨 Rock is about to bump against another rock! Done placing this rock.")
            return chamber, coords, True
    # safely move down
    for i, c in enumerate(coords):
        chamber[c[0]][c[1]] = "."
    for i, c in enumerate(coords):
        coords[i] = [c[0]+1, c[1]]
        chamber[c[0]+1][c[1]] = "@"
    return chamber, coords, False


# a rock "frozen" means @ is turned to # 
def freeze_rock(chamber, coords):
    for c in coords:
        chamber[c[0]][c[1]] = "#"
    return chamber

# execute main
if __name__ == '__main__':
    main()