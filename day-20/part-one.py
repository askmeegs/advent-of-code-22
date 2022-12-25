"""
This one returns the correct answer on small, but not on the full input :/ 

This is NOT the right answer, but it's the output I'm getting:

Hit the zero value, doing nothing
🏁 DONE: g1=-3673, g2=-9838, g3=-4776, sum=-18287

I think (??) my approach is ok -- if inefficient -- I think it's possible there is 
an off by one err..  or something that would work in a small example but not 
in a big one.. 
"""

import uuid

def main(): 
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    og = [int(line) for line in lines] 
    hashed = [] 
    # keep two maps in both directions 
    hash_to_actual = {}
    actual_to_hash = {}
    seen = set()
    zero_hash = "zzz"
    for i, o in enumerate(og):
        # have I seen this?
        if o in seen:
            print("I've seen {} before".format(o))
        seen.add(o)
        h = str(uuid.uuid4())
        hashed.append(h)
        hash_to_actual[h] = o
        actual_to_hash[o] = h 
        if o == 0:
            zero_hash = h
    print(actual_to_hash)
    for i, o in enumerate(og):
        # what is my hashed value? 
        my_hash = actual_to_hash[o] 
        # where is my hashed value? 
        my_index = hashed.index(my_hash)

        # should I move forward?
        if o > 0: 
            # perform "o" swaps forward
            for j in range(o):
                # swap the hashes
                hashed[my_index], hashed[(my_index + 1) % len(hashed)] = hashed[(my_index + 1) % len(hashed)], hashed[my_index]
                # update my index
                my_index = (my_index + 1) % len(hashed) 
        elif o < 0:
            # perform "o" swaps backward
            for j in range(abs(o)):
                # swap the hashes
                hashed[my_index], hashed[(my_index - 1) % len(hashed)] = hashed[(my_index - 1) % len(hashed)], hashed[my_index]
                # update my index
                my_index = (my_index - 1) % len(hashed)
        else: 
            print("Hit the zero value, doing nothing")

    # where is zero? 
    zero_index = hashed.index(zero_hash)

    # what is the index in hashed 1000 forward?
    g1_index = (zero_index + 1000) % len(hashed)
    g2_index = (zero_index + 2000) % len(hashed)
    g3_index = (zero_index + 3000) % len(hashed)

    # what is the value of the hash at that index?
    g1 = hash_to_actual[hashed[g1_index]]
    g2 = hash_to_actual[hashed[g2_index]]
    g3 = hash_to_actual[hashed[g3_index]]

    print("🏁 DONE: g1={}, g2={}, g3={}, sum={}".format(g1, g2, g3, g1+g2+g3))


# execute main
if __name__ == '__main__':
    main()