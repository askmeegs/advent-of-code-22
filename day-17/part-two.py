"""
initial cycle of 44 produces 55 height 

every following cycle of 35 produces 53 


2022 rocks is 
44 (55 height) 
+ 56 groups of 35 (2968)  


2968+55 

3068

+ 18 subsequent rocks 
"""


def main(): 
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]


# execute main
if __name__ == '__main__':
    main()