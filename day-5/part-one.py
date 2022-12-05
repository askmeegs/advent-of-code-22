"""
Task: predict output of a crane rearranging crates of supplies.

you're given 9 stacks of crates. (initial configuration)
then a rearrangement procedure.
when it says move "1" you move on crate FROM THE TOP OF ITS ORIGINAL STACK.
ONE CRATE AT A TIME.

RETURN: after the whole movement is done,  what crate ends up at the top of each stack? 
"""

"""
My crate format: 
zero indexed list 
c[0] = top of stack
"""

def main(): 
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    crates = [["G", "P", "N", "R"],
                ["H", "V", "S", "C", "L", "B", "J", "T"],
                ["L", "N", "M", "B", "D", "T"], 
                ["B", "S", "P", "V", "R"], 
                ["H", "V", "M", "W", "S", "Q", "C", "G"],
                ["J", "B", "D", "C", "S", "Q", "W"],
                ["L", "Q", "F"],
                ["V", "F", "L", "D", "T", "H", "M", "W"],
                ["F", "J", "M", "V", "B", "P", "L"]
            ]

    for line in lines[10:]:
        # strip whitespace from line 
        spl = line.split()
        # count of things to move = index 1 
        count = int(spl[1])
        origin = int(spl[3])
        dest = int(spl[5])
        for i in range(count):
            crates[dest-1] = [crates[origin-1].pop(0)] + crates[dest-1]

    result = ""
    # get the first item in each crate 
    for c in crates:
        result = result + c[0]
    print(result)

# execute main
if __name__ == '__main__':
    main()