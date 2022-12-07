from anytree import Node, RenderTree, find_by_attr, AsciiStyle, PreOrderIter
import uuid

def main(): 
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    
    curdir = lines[0].split(" ")[2]
    root = Node(curdir)
    stack = [curdir] 
    seen = {}
    for line in lines[1:]:
        if line == "$ cd ..":
            curdir = stack[0]
            stack = stack[1:]
            continue
        # if line starts with $ cd 
        elif line.startswith("$ cd"):
            # create a unique ID for this directory based on its direct parent
            # print(line)
            newdir = line.split(" ")[2]
            if newdir in seen:
                Node(newdir, parent=None)
            seen[newdir] = True
            # print("got new directory: {} with parent {}".format(newdir, find_by_attr(root, curdir)))
            if not find_by_attr(root, newdir):
                target = curdir.split("_")[0]
                Node(newdir + "_" + dir_id, parent=find_by_attr(root, target))
            stack = stack + [curdir]
            curdir = newdir
            continue
        # if line starts with $ ls
        elif line.startswith("$ ls"):
            continue
        elif line.startswith("dir"):
            continue
        else:
            size = int(line.split(" ")[0])
            # print("got new file: {} with parent {}".format(size, find_by_attr(root, curdir)))
            target = curdir.split("_")[0]
            Node(str(size), parent=find_by_attr(root, target))

    # write tree to file output.txt 
    with open('output.txt', 'w') as f:
        for pre, fill, node in RenderTree(root):
            f.write("%s%s\n" % (pre, node.name))
    """
    root
    ├── 14848514
    ├── 8504156
    ├── a
    │   ├── 29116
    │   ├── 2557
    │   ├── 62596
    │   └── e
    │       └── 584
    └── d
        ├── 4060174
        ├── 8033020
        ├── 5626152
        └── 7214296
    """
    # # I hate recursion and I will do everything I can to avoid it. I'm sorry. 
    # sums = {}
    # parentStack = []  # top = END 
    # preSum = 0
    # prevPre = -1 
    # for pre, fill, node in RenderTree(root):
    #     print("\n\nparent stack is {}, I'm looking at node {} with pre length {}, where prevPre is {}".format(parentStack, node.name, len(pre), prevPre))
    #     # process pre to deal with stack
    #     if len(pre) < prevPre:
    #         print("⭐️ time to pop parents off the stack")
    #         numParentsToPop = (prevPre - len(pre)) // 4
            
    #         print(numParentsToPop)
    #         for p in range(0, numParentsToPop):
    #             print("Popping {} off the stack ".format(parentStack[-1]))
    #             parentStack = parentStack[:-1]
    #             print("Parent stack is now {}".format(parentStack)) 
    #     prevPre = len(pre)
    #     # if a node is NOT an int, it's a dir
    #     try:
    #         int(node.name)
    #         mySize = int(node.name)
    #         print("📄 I'm a file with size {}".format(mySize))
    #         # my direct parent needs my size for its sum. 
    #         # print("I also need to add my file size to: {}".format(parentStack))
    #         for p in parentStack:
    #             if p not in sums:
    #                 print("🚨 dir {} is NOT in sums, so initializing it to {}".format(p, mySize))
    #                 sums[p] = mySize
    #             else:
    #                 print("✅   dir {} IS in sums (curVal={}), so adding {} to it".format(p, sums[p], mySize))
    #                 sums[p] += mySize
    #     except ValueError:
    #         if node.children:
    #             parentStack = parentStack + [node.name]
    #             sums[node.name] = 0
    #             preSum += len(pre)
    # print(calc_final_value(sums))

def calc_final_value(fs):
    print(fs)
    s = 0 
    for k, v in fs.items(): 
        if v <= 100000:
            print(v)
            s += v
    return s


# execute main
if __name__ == '__main__':
    main()