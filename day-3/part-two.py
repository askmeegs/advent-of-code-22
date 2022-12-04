"""
Elves in groups of 3. All elves have a badge identifying their group./
badges are item types 

Each set of 3 lines of input is a group of 3 elves

Find the item type shared between each group of 3. 
Sum them. 
"""

def main():
    # read input.txt into list of lines
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        # strip whitespace
        lines = [line.strip() for line in lines]
    
    # assign priority values 
    values = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
        "A": 27,
        "B": 28,
        "C": 29,
        "D": 30,
        "E": 31,
        "F": 32,
        "G": 33,
        "H": 34,
        "I": 35,
        "J": 36,
        "K": 37,
        "L": 38,
        "M": 39,
        "N": 40,
        "O": 41,
        "P": 42,
        "Q": 43,
        "R": 44,
        "S": 45,
        "T": 46,
        "U": 47,
        "V": 48,
        "W": 49,
        "X": 50,
        "Y": 51,
        "Z": 52
    }

    sum = 0 
    # iterate over lines in groups of 3
    for i in range(0, len(lines), 3):
        # get the 3 lines
        line1 = lines[i]
        line2 = lines[i+1]
        line3 = lines[i+2]
        # get the 3 sets of items
        items1 = set(line1)
        items2 = set(line2)
        items3 = set(line3)
        # get the intersection of the 3 sets
        intersection = items1.intersection(items2, items3)
        # this should just be 1 item 
        v = values[intersection.pop()]
        sum += v
    print(sum)

# execute main
if __name__ == '__main__':
    main()