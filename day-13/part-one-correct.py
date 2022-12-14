"""
Third try's the charm? 

in my first 2 attempts, I attempted to run logic 
using a combination of True/False and -1/0/1, where
0 represented uncertainty. 

I'm still not sure where my bug is, but I suspect
it's there. OR in the way I'm recursing. I think I 
have several lines of unnecessary code... 

Another area where my bug could be is, I'm iterating 
over all of L, recursively, instead of doing the right
recursive thing and paring down L as I go. 
so I should try to AVOID FOR LOOPS this time. 

Also instead, I'm ONLY going to use a number system.
Because we need 3 cases, T/F won't cut it. 

-1 is ordered. 
0 is still inconclusive or "sort of ordered."
1 is UNORDERED. 
"""

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
    sum = 0 
    for i, pair in enumerate(pairs):
        result = compare(pair[0], pair[1])
        if result == -1:
            sum += i+1
    print(sum)

def compare(L, R): 
    if L == []:
        # ran out of L but R is empty too --> "equals"
        if R == []:
            return 0 
        else: 
        # R is a list or an int, we ran out of L. 
            return -1 
    # L has items but we ran out of R --> unorderd
    if R == []:
        return 1
    if isinstance(L, list):
        if isinstance(R, list):
            result = compare(L[0], R[0])
            # is the result inconclusive?
            # if so, pare down and recurse 
            if result == 0:
                return compare(L[1:], R[1:])
            # else, we have a conclusive -1 or 1 
            return result 
        # if L is a list but R is int, convert R
        return compare(L, [R])
    # if L is an int and R is list, convert L 
    if isinstance(R, list):
        return compare([L], R)
    # base case, both are ints.
    if L < R:
        return -1 
    elif R < L: 
        return 1 
    else:
        return 0

# execute main
if __name__ == '__main__':
    main()