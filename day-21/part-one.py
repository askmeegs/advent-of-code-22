"""
Given a list of monkeys 

# = Monkey yells that number
aaaa + bbbb = Monkey waits for those monkeys to yell, then yells the sum 
aaaa - bbbb 
aaaa * bbbb
aaaa / bbbb

then the root yells its number 

Is this a tree problem? can I avoid recursion? only time will tell.... 

leaf nodes have numbers, parents have operations 
"""

from anytree import Node, RenderTree, DoubleStyle, PostOrderIter

def main(): 
    with open('input.txt', 'r') as f:
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
    print(RenderTree(root, style=DoubleStyle))
    
    # post order traversal 
    post = [node.name for node in PostOrderIter(root)]
    print(post)
    

    results = {} 
    for node in post:
        if node == "xroot":
            continue
        if isinstance(raw_nodes[node], int):
            results[node] = raw_nodes[node]
        else:
            op = raw_nodes[node][1]
            child1 = raw_nodes[node][0]
            child2 = raw_nodes[node][2]
            if op == "+":
                results[node] = results[child1] + results[child2]
            elif op == "-":
                results[node] = results[child1] - results[child2]
            elif op == "*":
                results[node] = results[child1] * results[child2]
            elif op == "/":
                results[node] = results[child1] / results[child2]
    print(results)
    print(results["root"])

# execute main
if __name__ == '__main__':
    main()