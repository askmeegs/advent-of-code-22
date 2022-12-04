"""
ANY overlap...
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
    
    pairsOverlap = 0
    for pair in sanitized:
        overlapSinglePair = False 
        iX = pair[0]
        iY = pair[1]
        jX = pair[2]
        jY = pair[3]
        if overlap(iX, iY, jX, jY) or overlap(jX, jY, iX, iY):
            overlapSinglePair = True 
            pairsOverlap += 1
        print("Pair is {}-{} and {}-{}: do the pairs overlap at all? {}\n".format(iX, iY, jX, jY, overlapSinglePair))
        
    print(pairsOverlap)

"""
.2345678...  2-8
...45678910..  4-10 

...45678910..  4-10 
.2345678...  2-8

YES

7-7
12-96 
"""

# check if two ranges overlap at all
def overlap(iX, iY, jX, jY):
    if iX <= jX and iY >= jY:
        return True
    if jX <= iX and jY >= iY:
        return True
    if jX <= iX and iX <= jY:
        return True
    if jX <= iY and iY <= jY:
        return True
    return False

# execute main
if __name__ == '__main__':
    main()