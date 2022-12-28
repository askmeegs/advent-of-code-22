"""
🐵 🗺️ 

        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5



^^ that is the map. 

. = open tile (can move over this), # = solid wall 

10R5L5R10L4R5L5 = path you must follow
alternating letters/numbers. 

number = # of tiles to move in the dir. you're facing 
    if you hit a wall, stop moving and go to the next instr. 

letter = turn in place (do not change cur tile)
    R = turn 90 degrees clockwise
    L = turn 90 degrees counter-clockwise


start at the top left of the map and start facing RIGHT --> 

the map wraps around itself. 
if you try to wrap around to a wall, stop. don't wrap around. 

your path on the map writes a password. find your final:
    - row  (1 indexed)
    - col (1 indexed)
    - facing: 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)

password = (1000 * row) + (4 * col) + facing
"""

def main(): 
    # instructions - parse 
   #  instr = "10R5L5R10L4R5L5"
    instr = "26R47R4R17L43L25L43L44R10R16L33L39L5L3R43L6L20R19R21R36R9L48R25L44R22R42R20L15R11R18L32L1R44L7R22L22L8R44L25R11L26L19L25R43R14R4R38R23R23R44R26L22L34R48R33R44L6L40R6R43R21R36L3L5L33L42R29R46R26L19L36L23L27L43R31L8R33L21R39R50L43R40R13L35R27L5R9R3R48R16L26R5R21R43L4L35L12L12L37L1L42R34R35R28R9L19L10L1R38R49R38L38L15L20R32R8R42R40R4L40L4L11L14L2L12R33L16R39R25R21R32L8L23R15L37L16L25R6R32L12R34L5L12R48R25L17L15R35R8R2L35L47L49L21L48R46L23R16R32L39L25R19L23L2R5R8L11L39L42L6L12R27L32L14L1R28L6L44R44L43R47R10R40L14R1R19R34L30R43L8L33L2R22R28R23R19R6L30L45L32L20L33L18R8R38R11L41L38L34R24L31R22R29R6L49L10L44R34L23L17R19R39L37L31R40L19R25R32L46L27L17R11R45R2R23L30R2L48R21L1R46R29L4R26L7R19R9R35L30R39L23R38R8R17R7L17L36L14L7R49L34L43R28R23R31L23R38R44R32L23R45L2L19L28L14L25L6L43L28R24L25R10L31R3L1L14L20L48R39R33L34L35L13R7R9R14R30R16L48L40L20L18R7R13L7L2L48L32R30L28L32R26L36R41L29L25L2L7R49L36R42R26L37R31R24R29L21L3L10L30R9R26R32R44R35L24R43R22R12L31R25R34R28L34L36L22L40L9L25R34L11R8R12R45L40R2L26R9L37L30L34R33R12R25L6L7R37L33L9R38L14R25R8L43R37R34L7L34R43R46L47L11L23L1L11R47R14L31R31R6R26R6L18L6L12L27L17R31L19R7L5L25L24R45L12L40L36L13R49R48L12L28L35L17R24L29R29L45R32L38L6L27R48L27R37L5R8L6R1R46R9L2L47L2R37R21R36R49R12R34L44L49R1R20R20R34R5R7R31L32R42R6R25L18L19L6L1L36L50L4L48R37L49R39L16R9R50R11L15R43R27L22R40R10R6R50L46L2R6R39L16L14L1L22L50R27L32R13R44R37R47L19R46R6R43L5L21L39R6L4R45R1L2L5R42R35L32L1L26L43R26L19R38R1R24R26L12L25R46R28R19R30R46R12R50L49R25L4L29R47R42L22L29R42L6R30L18R15R25L31L13L34R40R42L38L18R40L26R10R39L30R7R12L29R15R28L6L40L33L29R6L8L11L42L25L12R14L33R16L42L14R38L30L8L33R34L40L25R17R29L19L47R29L12L17R12L47R19R37R30R48L45R14L48R5R31R20L39R20R24R46R42L21L4R14R3L46R32R15L45L47R24L16R40R33L50L21R12R20R43L47R14L47R30R33R27R48R44L3L45R19L34L25L13R24R38R28L37R34L44R45L15R36R41R12R44R15L28R7L8L22R16R36R3L18R34R34L47R1R24L8R27L50L24L26L34R45R43R23R34L33L5L10R41L25R11L4R50R31R18L9R41L43R30R17L7L31L45R17R8R21R32R18R47R50R11R2L24R38L34R27L19R50L5L35R16L50R41L30L14L27R39L42R34R18L36L17L42L36L28L20L43L48R24R33R32R20L48L16R33L50L29R36L26L49R27R47R4L36L12R45R15L18R41R39L30R44L30R16R38R8R8L29L49L38L50R49R44R7L23R30R21L35L45R22R11R19R45L46L37R36L20L6L27R18L16R46L39L6L15L19R15L11L39R4R42R23R11R44L1R44L23R15L22R40L12R1R41L36L43L41R20R49L50R18R1R43R11L35R45L10L16R27R17L30R14R24R20L21R30L41R25R7R47R15R7R46R44R19R28L49L32R43R1L33L48L46L15R20R3L33L38R39R8R26R16L4L49R36R40R15L36L16L39R30R3L33L14R25L27R41L43R26R46R25L3L47R10L38L31R11R49L1R40R8R13L39L23R31R30R21L5L48R7L33L35L37L43L18R38L8L18R14R29R13L36L44L23L40L38R7R13R48R28R41R8L48L2L40L11R33L17R20R16R21L33L31L50L31R31R23L39L19R6R33R37L49L38R25L35L21R50R33R21R34R20R2L45R36R11R29L3L30R13R25L38L13L30L31R10R3L14R26L5R15R36R22R12L7R45L3L10R19L10R21R45R1R21L6R22L48R27L16L22R28R49L32L21R6R32R2R27R45R5R4R35R45L44L32L8L31R45L38R1L28L17L21L25R34R45R38L11R23L25L32L3R25L24L6L45L25R30L39R20R34L29R33R28R18R9L47L48L49L26R30L39R47R6L21R14L10R23R39L39R36R27R31R18L24L12L5R16R45L29L4R38L19L37R38L37R33R11L2R11R43R32L8L35L41L13L35R20L43L17R23R42L35L16R23R12L6R36R25L33L5R28L32R5R32L26R14L40L27L8L16L21R31R43L21R5R16R1R21R44R45R5R49R45L44R19L11R4L22R45R48R12R34R43R46L19R49R24R7L15R26R18R37L8R11R14L1R2L49R3L50R46R4L14R9R40L23L49R41L49R46R7R10L25R44L8R35L18L24L36L4R33L16R25R50R20R20R19R33R7R37R20R40R14R15R30R26R41R42R8R14R12R35L23L28L6R34L33L48L9L31R7L42L13L26L32L42L9R6R23R35R41L9R37R9L46R28R12L16R39L23L9L15R4R9R38R36R5R2L23L47R8R16L40R22R39R19L40R42L23L9L50R11L34L41L1R29L1R14L18L13R30R36L1L49R34R40R27L43L25R26L13R22R41R15R36R44R39L1R34R7L11L7R23L4L5R48L9R4R3L36L1R4L47L14L16L42L22R50L39L44L1R7R13L21L14R38R36L47R26L36R31R36L41R22L16L18R10R26R9R49R18R33R7R32R9R24R22L7R20L30L1L50L11R14R15R42L34R5L36R16R4L32L42L35L34R44L18L4R47L15R20L44L32R21L47L4L34R12L40L15L1L14L41R27L30L11L17L36L4R5R4L49R33R32L43R1L5R11L4L4L27R17L1L42L3R2L21L15R9L44R25L36R9L18L17R44L14L24L3R25R25L10R20L37R11R19L18R17R17L5L26R12L9L32R47L41L16R41L10R40R25R27R10R43L21L43L14R48R33L39L41L30R11L8L18L10R12R39L49R8R4R10R12L41L39R9L38L18L7R46L32L26L28R27L10R19R22R36R45R30L26L4L38L9R16R45L1L38R43L29L34R11L48R33L32R11R14L47L4L30R46R25L3L10R30L12L36R38L40R21L28R23L13R42R16L18L24R26L10L5L12R10L11R8R25L36L19L42R48L25R1R21L34L37R23R40L28R48R33L49R1L35R10L1L23R31L41L23R5R36L10L32L3L47R40L17L9L31R11R16R4L32L4L47L12L24L10R11R43L15L15L31L32L30R18L44R30R45L19L29R27R19L37R27L24L16R4R4R43R41R48L44R44L15L5R11R32R43R6R18L17R29L24L3L46R40L10L16R6R7R6R21R34R19R7R35L4L33R21L1R16R14R37L2R28R38R29L8R40R14R46L14L24L32L49R5R22L2L48L6R35R4L29R21R37L36R41L11R17R2L17L36L9R14L27R29L44L5R11R40L27L32L32R37R43L39L1L27L8L1R29L28L36R16L18R2R19R41R46R47L6R18L16R28L2R8R48L31L31L45R37L34R32L42L27R43R43L5L11R21L31L18L26R36L8L4L50R18L46L10R16L16L27R37L30L48R40R31L9R7L32R5R43R28R18L22R6L11L32L46L32L4R23L43R50L5R25R19L12R43L47L12L39L28R5R7L31R32R13L1R13L27R45R14R32R24L4R33L27L49L16L28L6R42L9R8R15L16L3R10L17L30L6R17R22R47R48L13L17R21L5R7R30R34L47L3R50R40R12L33L4L22R24L19L48L33L5R19R22R12L26R10R42L21L10R9R21L22R26L32L3R48L42L50L40R1R25R40R24L40R25L42R49R38R43L46R34R11L30R10R1R11L32L22R17R31L20R21L46R32L17L2R17L49R19L1R28L48R21L23R20R12L13R39R31R45L16R28R10R8R33L9L21R35R19L20L41R39L45L24L13R37R7R2R14R33R21L24R48R32R41L48L47L24L9R1R35R48R2L6L8L29L28R12R5L47R6L22L47L38L32L30R21L2R9R1L46L12R28L9R1R38L22L23L45L26R15R20R43L27L50L48L24L42R42R25L16R8L6R11L37L7L24R16R35L20R41R6L4R47L9L15L23R41L16R4R18L31L1R24L28R26L34R11L15R28L33R11R47R36L21R29L31L34L16L46R35L13R20L39L11L6R50L27L30L25R37R46L37L42L36L12R4R7R1R11R50R45L9R10L31R39R41L33R18R14R43L18R23L31L14L13L37L29L29L31L38R17L14L7L5L5R16R6R43L3R31L18L32L2L18R11L10R2R5R2R35R48R12R15L48R25R10L27R23L17L13L42R34R36R17R25L36L17L12L9L3L50L15L2L22L50R45L43L13L39"
    instr_list = [] 
    i = 0 
    while i < len(instr):
        char = instr[i]
        # if char is a number..
        if char.isdigit():
            # look ahead for more digits
            j = i+1 
            while j < len(instr) and instr[j].isdigit():
                char += instr[j]
                j += 1
            instr_list.append(int(char))
            i = j
            continue 
        else:
            instr_list.append(char)
            i += 1
  
    # populate map 
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    """
    # = wall 
    . = open 
    x = void 

    > = I was here, facing right
    < = I was here, facing left
    v = I was here, facing down
    ^ = I was here, facing up 
    """

    # create map
    map = []
    # what is the longest line? 
    lens = [len(line) for line in lines]
    max_row_length = max(lens)


    for line in lines:
        row = []
        i = 0 
        for char in line:
            if char == '#':
                row.append('#')
            elif char == '.':
                row.append('.')
            else:
                row.append('x')
            i += 1 
        if i > max_row_length:
            max_row_length = i
        if i < max_row_length:
            # pad the row with "x"
            while i < max_row_length:
                row.append('x')
                i += 1
        map.append(row)
    pretty_print(map)

    # what is the length of every row in the map?
    print("The map has {} rows.".format(len(map)))
    for row in map:
        print("Row length: {}".format(len(row)))

    # start at top left, facing right
    # facing: 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)

    row = 0
    col = 0
    facing = 0
    # figure out the real starting point - the first "." tile in row 1 
    for i in range(len(map[0])):
        if map[0][i] == '.':
            col = i
            break
    # execute instructions
    # print(instr_list)
    for instr in instr_list:
        # if instr is a letter, turn in place
        # DO NOT update row/col 
        if instr == 'R':
            facing = (facing + 1) % 4
            map[row][col] = ['>', 'v', '<', '^'][facing]
            continue 
        if instr == 'L':
            facing = (facing - 1) % 4
            map[row][col] = ['>', 'v', '<', '^'][facing]
            continue 
        # if instr is a number, move forward that many tiles
        # if you hit a wall, stop moving
        # if you hit the end of the map OR a void "x", wrap around 
            # mark where you were
            """
            Rules of movement:
            - if you hit a wall, stop moving and go to the next instr.
            - if you hit the end of the map OR a void "x", wrap around

        """
        for i in range(instr):
            # print("🔁 Moving 1 step {} (instr={}, i={})".format(['>', 'v', '<', '^'][facing], instr, i))
            # pretty_print(map)
            map[row][col] = ['>', 'v', '<', '^'][facing]
            if facing == 0:
                # what's to the right of us?
                # option 1: a void "x" OR the end - wrap around AS LONG AS there isn't a wall. 
                # wrap to the first "." we see after the void. 
                if col+1 >= len(map[0]) or map[row][col+1] == 'x':
                    temp_col = 0 
                    safe = True
                    # find the first non void character
                    while temp_col < len(map[0]) and map[row][temp_col] == 'x':
                        temp_col += 1
                        # if we hit a wall, stop moving
                        if map[row][temp_col] == '#':
                            safe = False
                            break 
                    if safe:
                        col = temp_col
                # option 2: a wall. STOP 
                elif map[row][col+1] == '#':
                    break
                # option 3: another open space. yay. move 
                else:
                    col += 1
            elif facing == 1:
                # what's below us?
                # option 1: a void "x" OR the end - wrap around AS LONG AS there isn't a wall. 
                # wrap to the first "." we see after the void. 
                if row+1 >= len(map) or map[row+1][col] == 'x':
                    temp_row = 0 
                    safe = True
                    # find the first non void character
                    while temp_row < len(map) and map[temp_row][col] == 'x':
                        temp_row += 1
                        # if we hit a wall, stop moving
                        if map[temp_row][col] == '#':
                            safe = False
                            break 
                    if safe:
                        row = temp_row
                # option 2: a wall. STOP 
                elif map[row+1][col] == '#':
                    break
                # option 3: another open space. yay. move 
                else:
                    row += 1
            elif facing == 2:
                # what's to the left of us?
                # option 1: a void "x" OR the end - wrap around AS LONG AS there isn't a wall. 
                # wrap to the first "." we see after the void. 
                if col-1 < 0 or map[row][col-1] == 'x':
                    temp_col = len(map[0]) - 1 
                    safe = True
                    # find the first non void character
                    while temp_col < len(map[0]) and map[row][temp_col] == 'x':
                        temp_col -= 1
                        # if we hit a wall, stop moving
                        if map[row][temp_col] == '#':
                            safe = False
                            break 
                    if safe:
                        col = temp_col
                # option 2: a wall. STOP 
                elif map[row][col-1] == '#':
                    break
                # option 3: another open space. yay. move 
                else:
                    col -= 1
            elif facing == 3:
                # what's above us?
                # option 1: a void "x" OR the end - wrap around AS LONG AS there isn't a wall. 
                # wrap to the first "." we see after the void. 
                if row-1 < 0 or map[row-1][col] == 'x':
                    temp_row = len(map) - 1
                    safe = True
                    # find the first non void character
                    while temp_row < len(map) and map[temp_row][col] == 'x':
                        temp_row -= 1
                        # if we hit a wall, stop moving
                        if map[temp_row][col] == '#':
                            safe = False
                            break 
                    if safe:
                        row = temp_row
                # option 2: a wall. STOP 
                elif map[row-1][col] == '#':
                    break
                # option 3: another open space. yay. move 
                else:
                    row -= 1

   
                
    
    # print final position
    print("FINAL MAP: ")
    pretty_print(map)
    print("\n")

    row += 1
    col += 1

    print("Final position: ({}, {})".format(row, col))
    print("Final facing: {}".format(facing))

    # print password
    password = (1000 * row) + (4 * col) + facing
    print("🏁 DONE: Password: {}".format(password))


def pretty_print(map):
    print("\n")
    for row in map:
        print(''.join([' ' if char == 'x' else char for char in row]))
    print("\n")
# execute main
if __name__ == '__main__':
    main()