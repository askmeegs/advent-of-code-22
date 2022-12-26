"""
root is now an equality test, not addition - 
listen to pppw and sjmn and checks that the numbers are equal

what number does "humn" need to yell in order for the equality test to match? 

I feel like this is the same problem just backwards... we know what root needs to be...
we have to reverse all the operations ... to end up with a leaf node. 

almost like a traversal but *ending* with humn ... 

IN SMALL... 
we need root's 2 children, pppw and sjmn, to have equal values. 
one of those children (in this case, pppw) contains humn which can be modified so that pppw's 
final value is equal to sjmn 

IN INPUT...
the total lineage of humn is:
['xroot', 'root', 'rvrh', 'zzfl', 'nntd', 'sqcv', 'tsws', 'nqzq', 'lbtc', 'vprg', 'lpdm', 'rczq', 'gchn', 'lqrl', 'twgl', 'rqdw', 'rzbv', 'fqbj', 'rdll', 'dbhj', 'cqsc', 'brzb', 'qdjw', 'qwql', 'tcqt', 'cjjw', 'thfm', 'smdc', 'gcvc', 'srwd', 'gprd', 'bpqn', 'hwbl', 'tnnz', 'ppnh', 'gtzj', 'wwpl', 'tnsg', 'mwrw', 'hcwn', 'pjhb', 'lbsc', 'czvw', 'glmj', 'zmdf', 'bmdq', 'dqtw', 'pbsw', 'mbmq', 'nhzv', 'jvmf', 'fmwr', 'bfss', 'mgrf', 'tvnr', 'rzmq', 'lddt', 'ndmz', 'pqbb', 'vrdj', 'mbwd', 'gvcm', 'pfbw', 'fqvn', 'pfqf', 'wjpg', 'nlrj', 'mqcz', 'sfhp', 'ghtq', 'gbjb', 'zctd']

root has children rvrh and hzgl 
humn is contained in the rvrh branch, so we need to match rvrh to hzgl's value 
"""


from anytree import Node, RenderTree, DoubleStyle, PostOrderIter, PreOrderIter

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
    # raw_nodes["xroot"] = ""
    # for pre, fill, node in RenderTree(root, style=DoubleStyle):
    #     print("{}{}: {}".format(pre, node.name, raw_nodes[node.name]))
    
    """
    maaaaaaaaath 

    we're trying to get to 150 

    pppw = (cczh  / lfqf)
                     lfqf=4
            sllz + lgvd
            sllz=4
                    ljgn * ptdq 
                    ljgn=2   ____ - dvpt 
                                     dvpt=3 


    sub the values.  
        pppw = (cczh  / 4)
            4 + lgvd
                 2 * ptdq =  
                       ____ - 3
        
        150 =  (((x - 3) * 2) + 4) / 4 
         150    = ((2x-6) + 4) / 4 
         600    = 2x - 2 
         602   = 2x
            301   = x
    
    how to turn that into code... 

    """
    target = 5697586809113 
    branch = nodes["rvrh"]
    for pre, fill, node in RenderTree(branch, style=DoubleStyle):
        print("{}{}: {}".format(pre, node.name, raw_nodes[node.name]))



    algebra = []
    pre = [node.name for node in PreOrderIter(branch)]
    branch_results = {}
    for node in pre:
        v = raw_nodes[node]
        branch_results[node] = v
    branch_results["humn"] = "x"
    print("POST TRAVERSAL: ")
    print(pre)

    prob = create_math_problem("rvrh", branch_results)
    
    # now we have a full algebra problem! 
    prob = str(target) + " = " + prob
    # find the value of x 
    print(prob)
    

"""
pppw: ['cczh', '/', 'lfqf']
╠══ cczh: ['sllz', '+', 'lgvd']
║   ╠══ sllz: 4
║   ╚══ lgvd: ['ljgn', '*', 'ptdq']
║       ╠══ ljgn: 2
║       ╚══ ptdq: ['humn', '-', 'dvpt']
║           ╠══ humn: 5
║           ╚══ dvpt: 3
╚══ lfqf: 4

POST TRAVERSAL:
['pppw', 'cczh', 'sllz', 'lgvd', 'ljgn', 'ptdq', 'humn', 'dvpt', 'lfqf']

pppw = []     /      [] 
      [] + []        4 


Don't actually RUN any math yet. Don't convert strings to ints... Just create the problem. 
"""
def create_math_problem(n, vals): 
    if n is None:
        return ""
    v = vals[n]
    # if it's a number or the variable, return it
    if isinstance(v, int) or v == "x":
        return str(v)
    # if it's an op, return the op and the next two items
    return "(" + create_math_problem(v[0], vals) + " " + v[1] + " " + create_math_problem(v[2], vals) + ")"
        





    
# execute main
if __name__ == '__main__':
    main()