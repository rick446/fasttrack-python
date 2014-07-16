mytree = ('root',
          ('child-L',
           ('child-LL', (), ()),
           ('child-LR', (), ())),
          ('child-R',
           ('child-RL', (), ()),
           ('child-RR', (), ())))

def postorder_tree_iter(node, level=0):
    if node:
        value, left, right = node
        for child_level, child_value in postorder_tree_iter(
              left, level+1):
            yield child_level, child_value
        for child_level, child_value in postorder_tree_iter(
              right, level+1):
            yield child_level, child_value
        yield level, value

for level, value in postorder_tree_iter(mytree):
    print ' ' * level, value
