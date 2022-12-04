"""
Each rucksack has 2 compartments.
It's supposed to be 1 item type per rucksack compartment. 


The input is a list of all items in each rucksack. 
1 rucksack = 1 line 
bisect each line into 2 compartments of equal string length

each compartment line only shares 1 item type with the other compartment 

Item types are a letter - case sensitive. (52 item types)
a-z = 1-26
A-Z = 27-52

Return the sum of item types values across all rucksacks. 
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
    for line in lines:
        # split line into two strings of equal length
        first = line[:len(line)//2]
        second = line[len(line)//2:]
        # what character is shared between the two strings?
        shared = set(first).intersection(set(second))
        # get first character in set
        shared = list(shared)[0] 
        shared_value = values[shared] 
        sum += shared_value
    print(sum)

# execute main
if __name__ == '__main__':
    main()