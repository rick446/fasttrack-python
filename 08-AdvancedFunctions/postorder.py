mytree = ('root', 
          ('child-L', (), ()), 
          ('child-R', 
           ('child-RL', (), ()),
           ('child-RR', (), ())))

def postorder_tree_map(function, node, level=0):
    value, left, right = node
    result = []
    if left:
        result += postorder_tree_map(function, left, level+1)
    if right:
        result += postorder_tree_map(function, right, level+1)
    result += [function(level, value)]
    return result
    
def print_node(level, value):
    print ('    ' * level) + repr(value)
    return value

postorder_tree_map(print_node, mytree)
