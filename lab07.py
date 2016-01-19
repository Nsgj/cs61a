__author__ = 'computer'
import inspect
# Tree definition - same Data Abstraction but different implementation from lecture
def tree(entry, subtrees=[]):
    #for subtree in subtrees:
    # assert is_tree(subtree)
    return lambda dispatch: entry if dispatch == 'entry' else list(subtrees)

def entry(tree):
    return tree('entry')

def subtrees(tree):
    return tree('subtrees')

def is_tree(tree):
    try:
        tree_data = inspect.getargspec(tree)
        assert tree_data == inspect.getargspec(lambda dispatch: None)
        return all([is_tree(subtree) for subtree in subtrees(tree)])
    except:
        return False

def is_leaf(tree):
    return not subtrees(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the entry.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(entry(t)))
    for subtree in subtrees(t):
        print_tree(subtree, indent + 1)

numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
## Trees ##

# Q1
# Q2
# Q3
def find(t, target):
    """Returns True if t contains a node with the value 'target' and False otherwise.

    """
    "*** YOUR CODE HERE ***"
    result = False
    if is_leaf(t):
        if entry(t) == target:
            return True
        else:
            return False
    elif entry(t) == target:
        return  True
    else:
        for i in subtrees(t):
            if find(i,target):
                return True
            else:
                continue
    result = bool(result)
    return  result

my_account = tree('kpop_king',
                        [tree('korean',
                             [tree('gangnam style'),
                               tree('wedding dress')]),
                        tree('pop',
                             [tree('t-swift',
                                   [tree('blank space')]),
                         tree('uptownfunk')])])

# Q4
def delete(t, target):
    root = entry(t)
    def help(t,target):
        new_subtree = []
        if is_leaf(t):
            if entry(t) == target:
                return []
            else:
                return [t]
        elif entry(t) == target:
            return []
        else:
            for i in subtrees(t):
                new_subtree += delete(i,target)
        return tree(entry(t),[new_subtree])
    return tree(root,[help(subtrees(t),target)])


my_account = tree('kpop_king',
                       [tree('korean',
                              [tree('gangnam style'),
                              tree('wedding dress')]),
                        tree('pop',
                             [tree('t-swift',
                                    [tree('blank space')]),
                               tree('uptownfunk')])])
new = delete(my_account, 'pop')
#print_tree(new)
