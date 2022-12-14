"""
Add Divider packets:
[[2]]
[[6]]

Then: put packets into correct order. 
Lowest to highest.

Then find where the divider packets ended up.
Multiply their indices (1-indexed). 
And return that value. 
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
    # put all pairs into one list of lists
    packetlist = []
    for pair in pairs:
        packetlist += pair 
    sorted = sort(packetlist)
    # find the indices of the divider packets
    # and multiply them.
    # find where [[2]] is 
    index1 = sorted.index([[2]])
    # find where [[6]] is
    index2 = sorted.index([[6]])
    print((index1+1) * (index2+1))

def sort(packets): 
    # base case: if we have 1 packet, return it
    if len(packets) == 1:
        return packets
    # if we have 2 packets, compare them and return
    if len(packets) == 2:
        result = compare(packets[0], packets[1])
        if result == -1:
            return packets 
        else:
            return [packets[1], packets[0]]
    # if we have more than 2 packets, 
    # sort the first half and the second half
    # and merge them. 
    if len(packets) > 2:
        # sort the first half
        firsthalf = sort(packets[:len(packets)//2])
        # sort the second half
        secondhalf = sort(packets[len(packets)//2:])
        # merge the two halves
        return merge(firsthalf, secondhalf)

def merge(L, R):
    # base case: if either list is empty, return the other
    if L == []:
        return R
    if R == []:
        return L
    # compare the first elements of L and R
    result = compare(L[0], R[0])
    # if L[0] is smaller, add it to the result list
    # and recurse on the rest of L and R
    if result == -1:
        return [L[0]] + merge(L[1:], R)
    # if R[0] is smaller, add it to the result list
    # and recurse on the rest of L and R
    if result == 1:
        return [R[0]] + merge(L, R[1:])
    # if the first elements are equal, 
    # add the first element of L to the result list
    # and recurse on the rest of L and R
    if result == 0:
        return [L[0]] + merge(L[1:], R)

# this func still holds. 
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