"""
task: reorder a list of packets to decode a message. 

given a list of pairs of packets: how many are in the right order? 

each list starts with [, ends with ] and contains 0 or more comma separated values, either:
     an integer 
     or another list 

you could see [7,7,7,7]  ("regular list")
or [[8,7,6]]  ("nested with many shell layers")
or [[1],[2,3,4]]  ("nested separate")
or [1,[2,[3,[4,[5,6,7]]]],8,9]  ("nested populated)
or [] ("Regular empty list")
or [[[]]] ("empty nested list")

given a pair that looks like: [1,1,3,1,1] vs [1,1,5,1,1] 
you iterate left to right and compare 0th to 0th, and so on.  ("left" vs "right")


if both vals are ints: 
    lower int must come before right. so if left < right, ✅ RIGHT order BREAK. else keep checking.
if both vals are lists:
    go left to right and compare all values (recursive case).
    if left side runs out of values first, ✅ RIGHT ORDER. 
    else if R side runs out first, 🚨 BREAK. WRONG. 
    if lists are the same length, keep going. 
if it's list vs. int: 
    convert the int to a list, 2 becomes [2] 
    and do the "both vals are lists case." ^^ 


TASK: COUNT HOW MANY PAIRS ARE IN THE RIGHT ORDER. 
RETURN THE SUM OF THEIR INDICES. (first pair index 1)
"""

import ast 

def main(): 
    with open('small.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        # get a list of pairs 
        pairs = [] 
        for i in range(0, len(lines)-1, 3):
            p0 = ast.literal_eval(lines[i])
            p1 = ast.literal_eval(lines[i+1])
            pairs.append([p0, p1]) 
        # track which are in the right vs. wrong order 
        tracker = {}
        for i, pair in enumerate(pairs):
            print("\n\n 🚀Outer loop on official pair: {} vs. {}".format(pair[0], pair[1]))
            tracker[i+1] = is_right_order(pair)
        

        # print the sum of the indices of the right order pairs
        print("🏁 DONE")
        print(tracker)
        print(sum([i for i, v in tracker.items () if v==True]))


def is_right_order(pair):
    left = pair[0]
    right = pair[1]
    print("Comparing pairs: {} vs. {}".format(left, right))
    # iterate over left. if left side runs out first, ✅ RIGHT ORDER. 
    for i, leftItem in enumerate(left): 
        print("🔄 For loop iteration, i={}".format(i))
        if i >= len(right):
            # left side still has values, but right side ran out. 
            print("🚨 right side ran out of values, wrong order!")
            return False 
        # otherwise, compare values. 
        rightItem = right[i]
        # are both leftItem and rightItem integers?
        if isinstance(leftItem, int) and isinstance(rightItem, int):
            if leftItem < rightItem:
                print("✅ left int > right int. RIGHT ORDER. BREAK.")
                return True
        # are both values lists? recurse.
        if isinstance(leftItem, list) and isinstance(rightItem, list):
            print("Running recursive case on: {} vs. {}".format(leftItem, rightItem))
            return is_right_order([leftItem, rightItem])
        # is one a list and the other an int?
        if isinstance(leftItem, list) and isinstance(rightItem, int):
            rightItem = [rightItem]
            print("Running recursive case on: {} vs. {}".format(leftItem, rightItem))
            return is_right_order([leftItem, rightItem])
        if isinstance(leftItem, int) and isinstance(rightItem, list):
            leftItem = [leftItem]
            print("Running recursive case on: {} vs. {}".format(leftItem, rightItem))
            return is_right_order([leftItem, rightItem])
    # if we  get out of the for loop, we went through ALL left values, so return true. 
    print("✅ left side ran out of values, right order!")
    return True 

# execute main
if __name__ == '__main__':
    main()