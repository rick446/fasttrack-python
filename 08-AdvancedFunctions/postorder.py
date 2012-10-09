mytree = ('root', 
          ('child-L',
           ('child-LL', (), ()),
           ('child-LR', (), ())),
          ('child-R', 
           ('child-RL', (), ()),
           ('child-RR', (), ())))

def postorder_tree_map(function, node, level=0):
    value, left, right = node
    result = []
    if left:
        result.extend(postorder_tree_map(function, left, level+1))
    if right:
        result.extend( postorder_tree_map(function, right, level+1))
    result.append(function(level, value))
    return result
    
def print_node(level, value):
    print ('    ' * level) + repr(value)
    return value

print postorder_tree_map(print_node, mytree)
