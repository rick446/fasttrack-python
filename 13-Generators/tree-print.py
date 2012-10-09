mytree = ('root', 
          ('child-L',
           ('child-LL', (), ()),
           ('child-RR', (), ())),
          ('child-R', 
           ('child-RL', (), ()),
           ('child-RR', (), ())))

def postorder_tree_iter(node, level=0):
    if node:
        value, left, right = node
        for item in postorder_tree_iter(left, level+1):
            yield item
        for item in postorder_tree_iter(right, level+1):
            yield item
        yield level, value
    
for level, node in postorder_tree_iter(mytree):
    print ' ' * level, node
