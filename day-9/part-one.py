"""
Ignore the rope metaphors- they're confusing. 

Imagine a worm or caterpillar, with a head and a tail.
The head moves and the tail follows.  "." represents the torso. 
Its body isn't infinitely flexible of course. 
The head and the tail must always be touching, or "connected" via torso. 

At most it can stretch like this T.H  - but the next move must be that the T follows H, so TH. 
The goal is that T must always touch H (either overlapping, in the same row/col, or diagonally touching)

Or 

T
H
.

T
.
H

.
T
H


If you ever see something like 

.H
T.

And H moves further away -- in this case UP 1  --  like 
.H
..
T.

Then T is allowed to move diagonally to be touching again - in this case,  up and to the right. 
.H
.T
..

The task is: assuming that H and T both start overlapping, like "H." 
You're given the movement sequences for HEAD. 
Track the movement of TAIL. 

Part one is to count the positions in the unbounded grid that the tail visited AT LEAST ONCE. So one or more times. 
"""

def main(): 
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]


    moves = []
    for line in lines:
        moves.append(line.split(' '))

     
    # imagine the head and the tail starting in the center of a positive-negative grid. 
    hI = 0 
    hJ = 0
    tI = 0
    tJ = 0   
    
    # because the space isn't bounded, let's not use a 2D array, but instead a series of index trackers. for head and tail. 
    # to track how many places Tail has visited, we'll use a nested dictionary. {i: j: #} for # times visited that cell. 
    v = {} 

    for move in moves:
        direction = move[0]
        distance = int(move[1])
        print("🐛\n New move (line). To start, head is at ({}, {}) and tail is at ({}, {}). v is {}".format(hI, hJ, tI, tJ, v)) 
        # every step within each movement must be counted - the tail must move alongside, and we must track everywhere the tail went. 
        step = distance 
        while step > 0:
            print("Head, move 1 step in {} direction!".format(direction))
            if direction == 'U':
                hI -= 1
            elif direction == 'D':
                hI += 1
            elif direction == 'L':
                hJ -= 1
            elif direction == 'R':
                hJ += 1
            print("Head done step, now at {}, {}. Tail, it's your turn to follow.".format(hI, hJ)) 

            """
            Tail movement behavior. 
            if the head and tail have the same coordinates, do nothing. 
            if the head is already directly up/down/left/right, do nothing.
            if the head is already diagonally touching, do nothing. 
            if the head is one away, up down left or right, eg. "T.H", advance the tail up down left or right by 1 
            if the head is a "knight's move" away, then do a diagonal "pawn" move, 1 step diagonally, to be directly next to head. 
            """
            if hI == tI and hJ == tJ:
                print("Tail is already overlapping head, do nothing.")
            elif hI == tI and hJ == tJ + 1:
                print("Tail is already directly right of head, do nothing.")
            elif hI == tI and hJ == tJ - 1:
                print("Tail is already directly left of head, do nothing.")
            elif hI == tI + 1 and hJ == tJ:
                print("Tail is already directly below head, do nothing.")
            elif hI == tI - 1 and hJ == tJ:
                print("Tail is already directly above head, do nothing.")
            elif hI == tI + 1 and hJ == tJ + 1:
                print("Tail is already diagonally below and right of head, do nothing.")
            elif hI == tI + 1 and hJ == tJ - 1:
                print("Tail is already diagonally below and left of head, do nothing.")
            elif hI == tI - 1 and hJ == tJ + 1:
                print("Tail is already diagonally above and right of head, do nothing.")
            elif hI == tI - 1 and hJ == tJ - 1:
                print("Tail is already diagonally above and left of head, do nothing.")
            elif hI == tI and hJ == tJ + 2:
                print("Tail is one step right of head, move tail right by 1.")
                tJ += 1
            elif hI == tI and hJ == tJ - 2:
                print("Tail is one step left of head, move tail left by 1.")
                tJ -= 1
            elif hI == tI + 2 and hJ == tJ:
                print("Tail is one step below head, move tail down by 1.")
                tI += 1
            elif hI == tI - 2 and hJ == tJ:
                print("Tail is one step above head, move tail up by 1.")
                tI -= 1
            # A knight has EIGHT moves. 
            # if the head is a knight's move away, then do a diagonal "pawn" move, 1 step diagonally, to be directly next to head.
            elif hI == tI + 2 and hJ == tJ + 1:
                print("Tail is one step below and right of head, move tail down and right by 1.")
                tI += 1
                tJ += 1
            elif hI == tI + 2 and hJ == tJ - 1:
                print("Tail is one step below and left of head, move tail down and left by 1.")
                tI += 1
                tJ -= 1
            elif hI == tI - 2 and hJ == tJ + 1:
                print("Tail is one step above and right of head, move tail up and right by 1.")
                tI -= 1
                tJ += 1
            elif hI == tI - 2 and hJ == tJ - 1:
                print("Tail is one step above and left of head, move tail up and left by 1.")
                tI -= 1
                tJ -= 1
            elif hI == tI + 1 and hJ == tJ + 2:
                print("Tail is one step right and below head, move tail right and down by 1.")
                tI += 1
                tJ += 1
            elif hI == tI - 1 and hJ == tJ + 2:
                print("Tail is one step right and above head, move tail right and up by 1.")
                tI -= 1
                tJ += 1
            elif hI == tI + 1 and hJ == tJ - 2:
                print("Tail is one step left and below head, move tail left and down by 1.")
                tI += 1
                tJ -= 1
            elif hI == tI - 1 and hJ == tJ - 2:
                print("Tail is one step left and above head, move tail left and up by 1.")
                tI -= 1
                tJ -= 1
            else:
                print("🚨 I couldn't find a move, this is a bug.")


            print("🐢 Tail done step, now at ({}, {}). Marking tail step location as visited".format(tI, tJ))
            if tI in v:
                if tJ in v[tI]:
                    v[tI][tJ] += 1
                else:
                    v[tI][tJ] = 1
            else:
                v[tI] = {tJ: 1}
            step -= 1
        print("✅ Done move. Head is at ({}, {}) and tail is at ({}, {})".format(hI, hJ, tI, tJ, v))

    # to get the final result, we'll count the number of keys for all "i" values. this is the # of places we've visited. 
    result = get_final_result(v) 
    print("🏁 # CELLS VISITED AT LEAST ONCE: {}".format(result))




def get_final_result(visited_dict): 
    # count the number of keys for all "i" values. this is the # of places we've visited at least once. (we don't care about values yet, not for part one) 
    result = 0 
    for i in visited_dict.keys(): 
        result += len(visited_dict[i].keys()) 
    return result

# execute main
if __name__ == '__main__':
    main()