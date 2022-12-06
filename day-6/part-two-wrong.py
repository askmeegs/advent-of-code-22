def main(): 
    with open('input.txt', 'r') as f:
        txt = f.read()
        txt = txt.strip()
    curMarker = {}
    markerString = ""
    # markerIndexes are 0, 1, 2, 3... 13 When you hit 14 and you haven't broken yet, you're done! 
    markerIndex = 0 
    # for loop over txt 
    for i, c in enumerate(txt):
        # print("\n\nLooking at character {}, markerString is {}, curMarker is: {}, markerIndex is: {}".format(c, markerString, curMarker, markerIndex))
        if c in curMarker:
            # print("⚠️ Character {} is already in curMarker! curMarker is now empty; markerIndex is 0".format(c))
            # RESET, found a duplicate char in curMarker 
            if markerIndex > 10:
                print("I reset with a marker length {}, string is {} at index {}, because I hit a new character {}".format(len(markerString), markerString, i, c))
            curMarker = {}
            markerString = ""
            markerIndex = 0 
            continue 
        else:
            curMarker[c] = True
            markerString += c 
            markerIndex += 1
            if markerIndex == 14:
                # print("🎉 Marker index is now 14, so I found a 14-character curMarker! {} It's at index {}".format(markerString, i+1))
                print(i+1)
                break
            else:
                # print("Still in the game, added c to curMarker, incremented marker index to {}. marker string is {}".format(markerIndex, markerString))
                continue 
    print(len(txt))
# execute main
if __name__ == '__main__':
    main()