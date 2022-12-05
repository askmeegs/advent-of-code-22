"""

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
        """
        instead of moving them one at a time, move them as a single block 
        """
        print("\n\n Moving {} from {} to {}".format(count, origin, dest)) 
        block = crates[origin-1][:count] 
        crates[origin-1] = crates[origin-1][count:]
        print("I have {} in my block, the origin is now {}".format(block, crates[origin-1]))

        crates[dest-1] = block + crates[dest-1]

    result = ""
    # get the first item in each crate 
    for c in crates:
        result = result + c[0]
    print(result)

# execute main
if __name__ == '__main__':
    main()