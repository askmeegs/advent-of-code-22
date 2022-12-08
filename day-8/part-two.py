"""
Scenic score..

Viewing distance: how many trees can you see? 
Stop if you reach a tree that is the SAME or TALLER than mine (but count it)
A tree on an edge will have at least one viewing distance of 0 

scenic score = multiply viewing distance in all directions 

Find the tree with the highest score. Return the score.  
"""

def main(): 
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    matrix = [] 
    for line in lines:
        row = [] 
        for tree in line:
            row.append(int(tree))
        matrix.append(row)

    count = 0 
    high_score = 0 
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[0])-1):
            score = scenic_score(matrix, i, j)
            if score > high_score:
                high_score = score
    print("I looked at {} trees".format(count))
    print("High score: {}".format(high_score))


"""
Viewing distance: how many trees can you see? 
Stop if you reach a tree that is the SAME or TALLER than mine (but count it)
A tree on an edge will have at least one viewing distance of 0 

scenic score = multiply viewing distance in all directions 

"""
def scenic_score(matrix, row, col):
    myVal = matrix[row][col]
    # ----- LEFT  -------------------------
    j = col-1 
    left = 0 
    # ITERATE 
    while j >= 0:
        left +=1 
        if matrix[row][j] >= myVal:
            break 
        j -= 1 
    
  # ----- RIGHT  -------------------------
    j = col+1
    right = 0 
    # ITERATE 
    while j < len(matrix[0]):
        right += 1 
        if matrix[row][j] >= myVal:
            break
        j += 1 


  # ----- ABOVE  -------------------------
    # RESET 
    i = row-1 
    above = 0 
    # ITERATE 
    while i >= 0: 
        above += 1 
        if matrix[i][col] >= myVal:
            break
        i -= 1 
   
 # ----- BELOW  -------------------------
    # RESET 
    i = row+1 
    below = 0 
    # ITERATE 
    while i < len(matrix):
        below +=1 
        if matrix[i][col] >= myVal:
            break
        i += 1 
    return above * below * left * right
# execute main
if __name__ == '__main__':
    main()