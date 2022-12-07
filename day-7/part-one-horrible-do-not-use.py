"""
ALL OF THIS IS GARBAGE


find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes.

$ cd /
$ cd a 
$ cd .. 
$ ls 

1234 file.txt
dir a



- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)


the input is already in a depth-first-search sequence, so we can just build the tree as we go.
"""

def main(): 
    with open('small.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        dirtree = [] 
        # assemble the directory tree
        # assume we are starting at cd / (that's line 0)
        # naive solution: have two dictionaries 
        """
        the first dictionary is a flat mapping of directory names to their children
        the second is a sum of INDIVIDUAL, not nested, sums of each lowest-level dir.  
        from there we can calculate the nested sum by spelunking through dirs_children and grabbing the sums as we go..
        """ 
        dirs_children = {} 
        leaf_dir_sums = {}
        prev_dir = "/"
        cur_dir = "/"
        # init 
        dirs_children[cur_dir] = []
        for line in lines[1:]:
            # print("line is {}, cur dir is: {}, dirs_children is: {}, leaf_dir_sums is: {}".format(line, cur_dir, dirs_children, leaf_dir_sums))
            words = line.split(" ")
            if words[0] == "dir": 
                val = dirs_children[cur_dir] 
                val.append(words[1])
                dirs_children[cur_dir] = val
                dirs_children[words[1]] = []
            elif words[1] == "ls":
                continue 
            elif words[1] == "cd": 
                if words[2] == "..":
                    cur_dir = prev_dir 
                else:
                    prev_dir = cur_dir
                    cur_dir = words[2]
                    leaf_dir_sums[cur_dir] = 0 
            else:
                # process file
                size = int(words[0]) 
                if cur_dir in leaf_dir_sums: 
                    leaf_dir_sums[cur_dir] += size
                else:
                    leaf_dir_sums[cur_dir] = size

        print("\n\nleaf dir sums: {}".format(leaf_dir_sums))
        print("\n\ndirs children: {}".format(dirs_children))
        fs = calc_final_sums(dirs_children, leaf_dir_sums)
        print("final sums, with recursive adding: {}".format(fs))
        final_value = calc_final_value(fs)
        print("✅ final value is: {}".format(final_value))

# recursive function to calculate final sums 
def calc_final_sums(dirs_children, leaf_dir_sums):
   #  print("Entered calc final sums. dirs_children is: {}, leaf_dir_sums is: {}".format(dirs_children, leaf_dir_sums))
    final_sums = {}
    for dir in dirs_children.keys():
        starting_sum = 0
        # print("\n\n🏁 Starting recursion for dir: {}. My starting parameters are, MY DIRS_CHILDREN: {}, STARTING SUM: {}, LEAF DIR SUMS: {}, DIRS CHILDREN REF: {}".format(dir, dirs_children[dir], starting_sum, leaf_dir_sums, dirs_children))
        final_sums[dir] = helper(dir, dirs_children[dir], starting_sum, leaf_dir_sums, dirs_children)
    return final_sums 

"""
Recursive function to compute the sums.
The first two parameters are trackers: who am I now? (my children), what is my current recursive sum? of myself and all my children?
The second two are for reference, to allow for recursion to continue. 
"""
def helper(cur_dir, cur_children, my_sum, leaf_dir_sums, dirs_children):
    print("\n\nHi, I'm {}. My children are {}".format(cur_dir, cur_children))
    # base case 
    if len(cur_children) == 0:
        print("I have no children, exiting recursion, my final sum is {}".format(cur_dir, my_sum))
        return leaf_dir_sums[cur_dir]
    # # recursive case
    for child in cur_children:
        my_sum += leaf_dir_sums[child]
        print("I'm about to run the helper with on dirs: {}, my current sum: {}".format(dirs_children[child], my_sum))
        result = helper(child, dirs_children[child], my_sum, leaf_dir_sums, dirs_children)
        print("I got a result {}".format(result))
        print("I'm about to add my current sum, {}, to my childrens' result, {}".format(my_sum, result))
        my_sum += result
    print("Exiting recursion, my_sum is {}".format(my_sum))
    return my_sum
    
# calculate final value: sum of all of the directories with a total size of at most 100000
def calc_final_value(fs):
    print(fs)
    s = 0 
    for k, v in fs.items(): 
        if v <= 100000:
            s += v
    return s

# execute main
if __name__ == '__main__':
    main()