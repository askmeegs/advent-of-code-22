"""
Trees have height 0-9 
A tree is visible if  other trees between it and the edge are SHORTER
(Look up, down, left, right)


All edge trees are visible. Look only at interior trees. 

30373
25512
65332
33549
35390

Top-right 5 IS visible from left and top.. 
Top right 1 is NOT visible from any direction.

Count the total # of trees visible. 
AKA the sum of all perimeter trees
And the sum of all interior trees that are visible from at least one direction.
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
    # 99 x 99 
    visible = 392 # start with # of perimeter trees 
    count = 0 
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[0])-1):
            count = count + 1 
            print("\nChecking if {} is visible, row={}, col={}".format(matrix[i][j], i, j))
            # check if visible
            if is_visible(matrix, i, j):
                print("✅ Visible")
                visible += 1
            else:
                print("❌ Not visible")
    print("I looked at {} trees".format(count))
    print("Visible: {}".format(visible))

# 30373
# 25512
# 65332
# 33549
# 35390
def is_visible(matrix, row, col):
    myVal = matrix[row][col]
    # go left
    # row = i 
    # col = j 

    # ----- LEFT  -------------------------
    # RESET 
    j = col-1 
    count = 0 
    countShorter = 0
    # ITERATE 
    while j >= 0:
        count +=1 
        if matrix[row][j] < myVal:
            countShorter += 1 
        j -= 1 
    if countShorter == count:
        return True 
    
  # ----- RIGHT  -------------------------
    # RESET 
    j = col+1
    count = 0 
    countShorter = 0  
    # ITERATE 
    while j < len(matrix[0]):
        count +=1 
        if matrix[row][j] < myVal:
            countShorter += 1 
        j += 1 
    if countShorter == count:
        return True 

  # ----- ABOVE  -------------------------
    # RESET 
    i = row-1 
    count = 0 
    countShorter = 0  
    # ITERATE 
    while i >= 0: 
        count +=1 
        if matrix[i][col] < myVal:
            countShorter += 1 
        i -= 1 
    if countShorter == count:
        return True 
   
 # ----- BELOW  -------------------------
    # RESET 
    i = row+1 
    count = 0 
    countShorter = 0  
    # ITERATE 
    while i < len(matrix):
        count +=1 
        if matrix[i][col] < myVal:
            countShorter += 1 
        i += 1 
    if countShorter == count:
        return True 
   
    return False 

# execute main
if __name__ == '__main__':
    main()