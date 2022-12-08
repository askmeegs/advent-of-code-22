"""
file system has total space 70,000,000
we need unused space of 30,000,000

find a dir that will free up enough space 

Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update.
WHAT IS ITS SIZE?
"""

def main(): 
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]


# execute main
if __name__ == '__main__':
    main()