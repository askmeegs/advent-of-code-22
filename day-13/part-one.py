import ast 

def main(): 
    with open('input.txt', 'r') as f:
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


# from the outer loop, a pair is always list vs. list. 
# returns a definitive true of false 
def is_right_order(pair):
    left = pair[0]
    right = pair[1]
    print("\n🚀 OUTER LOOP: Comparing left: {} to right: {}".format(left, right))
    for i, lItem in enumerate(left):
        print("🔄 For loop iteration.") 
        if i >= len(right):
            print("🚨 right side ran out of values, wrong order! definite false in outer loop.")
            return False   
        rItem = right[i] 
        print("🔎 Comparing left item: {} to right item: {}".format(lItem, rItem))
        if isinstance(lItem, int) and isinstance(rItem, int):
            if lItem < rItem:
                print("✅ left int < right int. RIGHT ORDER. BREAK.")
                return True
            elif lItem > rItem:
                print("🚨 left int > right int. WRONG ORDER. BREAK.")
                return False
            else:
                continue
        if isinstance(lItem, int) and isinstance(rItem, list):
            lItem = [lItem]
        if isinstance(lItem, list) and isinstance(rItem, int):
            rItem = [rItem]
        helperResult = helper([lItem, rItem])
        if helperResult == -1:
            return False
        elif helperResult == 1:
            return True
        else: # helper returned 0 
            continue
    # "ran out of left items condition"
    print("✅ ran out of left items, outer loop. BREAK.")
    return True 


# returns -1 if wrong, 1 if right, 0 if unsure 
def helper(pair):
    left = pair[0]
    right = pair[1]
    # if right is of type list 
    if isinstance(right, list):
        if len(right) == 0:
            return -1
    if isinstance(left, int) and isinstance(right, list):
        left = [left]
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1 
        elif left > right:
            return -1  
        else:
            return 0 
    for i, leftItem in enumerate(left):
        if i >= len(right):
            return -1
        rightItem = right[i]
        if isinstance(leftItem, int) and isinstance(rightItem, int):
            if leftItem < rightItem:
                return 1
            elif leftItem > rightItem:
                return -1
            else:
                continue
        if isinstance(leftItem, list) and isinstance(rightItem, int):
            rightItem = [rightItem]
        if isinstance(leftItem, list) and isinstance(rightItem, int):
            leftItem = [leftItem]
        return helper([leftItem, rightItem])
    return 1




# execute main
if __name__ == '__main__':
    main()