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
        count = 0 
        pairs = pairs[147:]
        for i, pair in enumerate(pairs):
            count += 1 
            result = is_right_order(pair)
            tracker[i+1] = result
            print("🏆 Result of the whole is_right_order on pair {} vs. {} is: {}".format(pair[0], pair[1], result))
        

        # print the sum of the indices of the right order pairs
        print("🏁 DONE")
        print("I looked at {} pairs. There are {} keys in tracker".format(count, len(tracker)))
        print(tracker)
        print(sum([i for i, v in tracker.items () if v==True]))


# from the outer loop, a pair is always list vs. list. 
# returns a definitive true of false 
def is_right_order(pair):
    left = pair[0]
    right = pair[1]
    print("\n🚀 START PAIR: Comparing left: \n{} \nto right: \n{}".format(left, right))
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
    print("🤿 start helper on left: {} and right: {}".format(left, right))
    # if right is of type list 
    if isinstance(right, list):
        if len(right) == 0:
            print("🚨 right is empty list, ran out of right items. WRONG ORDER. BREAK return -1.")
            return -1
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            print("✅ L and R are ints, L={} is less than R={}, RIGHT ORDER. BREAK return 1.".format(left, right))
            return 1 
        elif left > right:
            print("🚨 L and R are ints, L={} is greater than R={}, WRONG ORDER. BREAK return 1.".format(left, right))
            return -1  
        else:
            print("🤨 L and R are both ints, but they're equal, L={} and R={}, UNSURE. BREAK return 0.".format(left, right))
            return 0 
    if isinstance(left, list) and isinstance(right, int):
        right = [right]
    if isinstance(left, int) and isinstance(right, list):
        left = [left]
    # now we can assume both are lists. iterate over left. 
    for i, leftItem in enumerate(left):
        if i >= len(right):
            return -1
        rightItem = right[i]
        result = helper([leftItem, rightItem])
        if result == -1:
            return -1
        elif result == 1:
            return 1
        else:
            continue
    print("✅ ran out of left items, right order, BREAK return 1.")
    return 1




# execute main
if __name__ == '__main__':
    main()