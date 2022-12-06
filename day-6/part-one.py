"""
signal = stream of characters the device receives one at a time. 
detect a start of packet marker , which is a sequence of 4 characters, all different 

find the # of characters from the beginning to the end of the first 4-character SOP marker 
NOT the index, it would be i+1 
"""


def main(): 
    with open('input.txt', 'r') as f:
        txt = f.read()
        txt = txt.strip()
        print(len(txt))
    curMarker = {}
    # markerIndexes are 0, 1, 2, 3. When you hit 4 and you haven't broken yet, you're done! 
    markerIndex = 0 
    # for loop over txt 
    for i, c in enumerate(txt):
        if c in curMarker:
            # RESET, found a duplicate char in curMarker 
            curMarker = {}
            markerIndex = 0 
            continue 
        else:
            curMarker[c] = True 
            markerIndex += 1
            if markerIndex == 4:
                print(i+1)
                break

# execute main
if __name__ == '__main__':
    main()