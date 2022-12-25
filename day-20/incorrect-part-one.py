"""
Given a list of positive or negative integers, 
The list is circular (wraps around itself)

to mix the file, move each number forward or backward in 
the file a # of positions equal to the value of the number being moved. 

The numbers should be moved in the order they originally appear in the encrypted file.
(Keep a second copy)
"""

def main(): 
    with open('small.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    og = [int(line) for line in lines] 
    copy = [int(line) for line in lines]

    # also track the rest of the values ... 
    # {"hashvalue": ["actual_value", "og_index", "cur_copy_index"]}
    zero_hash = "zzz"
    hash = {}
    for i, o in enumerate(og):
        h = str(o) + str(i)
        hash[h] = [o, i, i] 
        if o == 0:
            zero_hash = h

    print("🥚 This is the OG list:")
    print(og)
    print(hash)
    print("The zero hash is: {}".format(zero_hash))
    # for each value in og, move its current position in copy 
    for i, cur_value in enumerate(og):
        cur_hash = str(cur_value) + str(i) 
        cur_index = hash[cur_hash][2]
        print("\n\n New iteration, I'm on og i={} actual value {}, currently located at index {} in copy".format(i, cur_value, cur_index))
        if cur_value > 0: 
            # move o forward in copy by o 
            print("Moving forward...")
            for j in range(cur_value):
                print("Moving forward by 1")
                # swap with the item in front of it and update BOTH their cur indices 
                front_index = (cur_index + 1) % len(copy)
                front_value = copy[(cur_index + 1) % len(copy)]

                # update hash 
                front_hash = str(front_value) + str(front_index)
                hash[front_hash][2] = cur_index
                hash[cur_hash][2] = front_index

                # execute the swap      
                copy[cur_index], copy[front_index] = copy[front_index], copy[cur_index]

                print("cur_index is now {}".format(hash[cur_hash][2]))
        elif cur_value < 0:
            # move backward 
            print("Moving backward...")
            for j in range(abs(o)):
                print("Moving backward by 1")
                behind_index = (cur_index - 1) % len(copy)
                behind_value = copy[(cur_index - 1) % len(copy)]

                # update hash 
                behind_hash = str(behind_value) + str(behind_index)
                hash[behind_hash][2] = cur_index
                hash[cur_hash][2] = behind_index

                # execute the swap      
                copy[cur_index], copy[behind_index] = copy[behind_index], copy[cur_index]


                print("cur_index is now {}".format(hash[cur_hash][2])) 
        else:
            print("Hit the zero value! Doing nothing...")
        print("Iteration done, copy is now: {}".format(copy))

    # where is zero? 
    zero_index = hash[zero_hash][2] 
    g1 = copy[(zero_index + 1000) % len(copy)]
    g2 = copy[(zero_index + 2000) % len(copy)]
    g3 = copy[(zero_index + 3000) % len(copy)]
    print("g1={}, g2={}, g3={}".format(g1, g2, g3))
    print(g1+g2+g3)

# execute main
if __name__ == '__main__':
    main()