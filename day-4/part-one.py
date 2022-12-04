"""
Camp cleanup 

Every elf is assigned a range of section IDs of the campsite, but some overlap. 

Input: set of section assignment pairs. 
All elves line up. section assignments within the first pair... second pair.. etc. 

First, find how many pairs where one range FULLY CONTAINS another. 
"""


def main(): 
    # read input into list of lines 
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        # strip whitespace 
        lines = [line.strip() for line in lines]
        # split by comma
        lines = [line.split(',') for line in lines] 
        sanitized = []
        for pair in lines:
            temp = []
            for item in pair:
                spl = item.split('-')
                temp = temp + [int(spl[0]), int(spl[1])]
            sanitized.append(temp)
    
    pairsFullyContains = 0
    for pair in sanitized:
        fcPair = False 
        iX = pair[0]
        iY = pair[1]
        jX = pair[2]
        jY = pair[3]
        if fullyContains(iX, iY, jX, jY) or fullyContains(jX, jY, iX, iY):
            fcPair = True 
            pairsFullyContains += 1
        # print("Pair is {}-{} and {}-{}: does one pair fully contain another? {}\n".format(iX, iY, jX, jY, fcPair))
        
    print(pairsFullyContains)

"""
.2345678.  2-8
..34567..  3-7
"""

def fullyContains(iX, iY, jX, jY):
    if iX <= jX and iY >= jY:
        return True
    if jX <= iX and jY >= iY:
        return True
    return False

# execute main
if __name__ == '__main__':
    main()