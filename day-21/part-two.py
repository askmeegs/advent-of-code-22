"""
root is now an equality test, not addition - 
listen to pppw and sjmn and checks that the numbers are equal

what number does "humn" need to yell in order for the equality test to match? 
"""


from anytree import Node, RenderTree, DoubleStyle, PostOrderIter

def main(): 
    with open('small.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    raw_nodes = {}
    for line in lines:
        line = line.split(": ")
        name = line[0]
        value = line[1]
        # if value is an int
        if value.isdigit():
            # create a leaf node 
            dig = int(value) 
            raw_nodes[name] = dig 
        else:
            op = value.split(" ") 
            raw_nodes[name] = op 
    # draw the tree by populating every node as a leaf node 
    # then iterate through all the nodes, and if it's an op, it has TWO CHILDREN 
    # if it's a number, it has no children

    # create a root node
    root = Node("xroot")
    # create a dict of nodes pretending they're all leaf nodes
    nodes = {}
    for key, value in raw_nodes.items():
        if isinstance(value, int):
            nodes[key] = Node(key, parent=root)
        else:
            nodes[key] = Node(key, parent=root)
    # then correctly populate the tree's vertices 
    # iterate through all the nodes, and if it's an op, it has TWO CHILDREN
    for key, value in raw_nodes.items():
        a = raw_nodes[key]
        if isinstance(a, int):
            continue
        else:
            # get the two children 
            child1 = a[0]
            child2 = a[2]
            # add the children to the node 
            nodes[key].children = [nodes[child1], nodes[child2]]
    # print the tree
    raw_nodes["xroot"] = ""
    for pre, fill, node in RenderTree(root, style=DoubleStyle):
        print("{}{}: {}".format(pre, node.name, raw_nodes[node.name]))
    
    # post order traversal 
    # post = [node.name for node in PostOrderIter(root)]
    # print(post)



    
# execute main
if __name__ == '__main__':
    main()