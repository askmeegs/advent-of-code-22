"""
GREAT BIG SNAKE 

Now imagine a worm with more joints.
Instead of a head and a tail, you have a head, tail, and 8 joints in between.
For a total of 10. 

The head still moves however it wants.
Each subsequent 9 items move with the same behavior. 
Each knot follows the one DIRECTLY IN FRONT OF IT. 

if the knots are numbered 0-9... 0 is head, 9 is tail. 
0 moves a step, 1 follows.
1 moves a step, 2 follows... 

all the way to...
8 moves a step, 9 (tail) follows. this is the place to track in "v." 

There is a new tail, knot 10. It moves stepwise after all 9 have moved. 
The task is STILL to track this tail. 
"""

def main(): 
    with open('small-part-two.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    moves = []
    for line in lines:
        moves.append(line.split(' '))

     
    # track positions like this, instead of using const trackers. 
    # 10 knots total. index 0 is head. index 9 is tail. 
    positions = [
                [0, 0], 
                [0, 0],
                [0, 0],
                [0, 0],
                [0, 0],
                [0, 0],
                [0, 0],
                [0, 0],
                [0, 0],
                [0, 0]
    ]

    v = {0: {0: 1}} # still track tail visited like before. 
    for move in moves[:2]:
        direction = move[0]
        distance = int(move[1])
        print("\n\n ⭐️ New Move: head moves {} {}. Starting positions:".format(direction, distance))
        print_positions(positions)
        positions, v = execute_move(direction, distance, positions, v) 
    result = get_final_result(v)
    print(v)
    print(result)


def execute_move(direction, distance, positions, v):
    step = distance 
    while step > 0:
        positions, v = execute_step(direction, positions, v)
        step -= 1 
    return positions, v 


def execute_step(direction, positions, v):
    print("\n 👟 New step. Head moves 1 in {}".format(direction))
    # the head -- the real head -- moves.
    hI = positions[0][0]
    hJ = positions[0][1]
    if direction == 'U':
        hI += 1
    elif direction == 'D':
        hI -= 1
    elif direction == 'L':
        hJ -= 1
    elif direction == 'R':
        hJ += 1
    positions[0] = [hI, hJ]
    

    # now execute a series of follows. the subsequent 9 items will follow the one in front of them. 
    for cur_head_index in range(0, len(positions)-1):
        cur_head = positions[cur_head_index]
        cur_tail = positions[cur_head_index + 1] 

        print("\tAbout to run a follow where cur head is #{} and has position {}. Cur tail is #{} and has position {}".format(cur_head_index, cur_head, cur_head_index+1,  cur_tail))

        cur_head, cur_tail = follow(cur_head, cur_tail)
        # update current locations
        positions[cur_head_index] = cur_head
        positions[cur_head_index + 1] = cur_tail

        # if I'm the REAL tail, track where I've been. 
        if cur_head_index+1 == len(positions)-1:
            tI = cur_tail[0]
            tJ = cur_tail[1]
            if tI in v:
                if tJ in v[tI]:
                    v[tI][tJ] += 1
                else:
                    v[tI][tJ] = 1
            else:
                v[tI] = {tJ: 1}
    print("\tEnd of step. positions is:") 
    print_positions(positions)
    return positions, v

def follow(cur_head, cur_tail):
    hI = cur_head[0]
    hJ = cur_head[1]
    tI = cur_tail[0]
    tJ = cur_tail[1]

    # then move cur tail 
    if hI == tI and hJ == tJ:
        print("❌ head is already overlapping tail, do nothing.")
    elif hI == tI and hJ == tJ + 1:
        print("❌head is already directly right of tail, do nothing.")
    elif hI == tI and hJ == tJ - 1:
        print("❌head is already directly left of tail, do nothing.")
    elif hI == tI + 1 and hJ == tJ:
        print("❌head is already directly above tail, do nothing.")
    elif hI == tI - 1 and hJ == tJ:
        print("❌head is already directly below tail, do nothing.")
    elif hI == tI + 1 and hJ == tJ + 1:
        print("❌head is already diagonally above and right of tail, do nothing.")
    elif hI == tI + 1 and hJ == tJ - 1:
        print("❌head is already diagonally above and left of tail, do nothing.")
    elif hI == tI - 1 and hJ == tJ + 1:
        print("❌head is already diagonally below and right of tail, do nothing.")
    elif hI == tI - 1 and hJ == tJ - 1:
        print("❌head is already diagonally below and left of tail, do nothing.")
    elif hI == tI and hJ == tJ + 2:
        print("head is two step right of tail, move tail right by 1. ➡️")
        tJ += 1
    elif hI == tI and hJ == tJ - 2:
        print("head is two step left of tail, move tail left by 1. ⬅️")
        tJ -= 1
    elif hI == tI + 2 and hJ == tJ:
        print("head is two step above tail, move tail up by 1. ⬆️")
        tI += 1
    elif hI == tI - 2 and hJ == tJ:
        print("head is two step below tail, move tail down by 1. ⬇️")
        tI -= 1
    # A knight has EIGHT moves. 
    # if the head is a knight's move away, then do a diagonal "pawn" move, 1 step diagonally, to be directly next to head.
    elif hI == tI + 2 and hJ == tJ + 1:
        print("♞ head is two step above and 1 right of tail, move tail up and right by 1. ↗️ ")
        tI += 1
        tJ += 1
    elif hI == tI + 2 and hJ == tJ - 1:
        print("♞ head is two step above and 1 left of head, move tail up and left by 1. ↖️")
        tI += 1
        tJ -= 1
    elif hI == tI - 2 and hJ == tJ + 1:
        print("♞ head is two step down and 1 right of head, move tail down and right by 1. ↘️ ")
        tI -= 1
        tJ += 1
    elif hI == tI - 2 and hJ == tJ - 1:
        print("♞ head is two step down and 1 left of head, move tail down and left by 1. ↙️")
        tI -= 1
        tJ -= 1
    elif hI == tI + 1 and hJ == tJ + 2:
        print("♞ head is one step above and 2 right of head, move tail up and right by 1. ↗️")
        tI += 1
        tJ += 1
    elif hI == tI - 1 and hJ == tJ + 2:
        print("♞ head is one step down and 2 right of head, move tail down and right by 1. ↘️")
        tI -= 1
        tJ += 1
    elif hI == tI + 1 and hJ == tJ - 2:
        print("♞ head is one step above and 2 left of head, move tail up and left by 1. ↖️")
        tI += 1
        tJ -= 1
    elif hI == tI - 1 and hJ == tJ - 2:
        print("♞ head is one step down and 2 left of head, move tail down and left by 1. ↙️")
        tI -= 1
        tJ -= 1
    else:
        print("\t⚠️ no move recognized, this is a bug.") 

    return [hI, hJ], [tI, tJ]

def get_final_result(visited_dict): 
    # count the number of keys for all "i" values. this is the # of places we've visited at least once. (we don't care about values yet, not for part one) 
    result = 0 
    for i in visited_dict.keys(): 
        result += len(visited_dict[i].keys()) 
    return result

def print_positions(positions):
    items = ["H", "1", "2", "3", "4", "5", "6", "7", "8", "T"]
    for i, item in enumerate(items):
        print("\t{}: {}".format(item, positions[i]))

# execute main
if __name__ == '__main__':
    main()