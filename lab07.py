## Trees ##

# Q1
def make_pytunes(username):
    """Return a pyTunes tree as shown in the diagram.

    >>> pytunes = make_pytunes('i_love_t_swift')
    >>> print_tree(pytunes)
    i_love_t_swift
      pop
        taylor swift
          1989
            bad blood
        2015 pop mashup
      hip hop
        nicki minaj
          anaconda
    """
    "*** YOUR CODE HERE ***"


# Q2
def num_songs(t):
    """Return the number of songs in the pyTunes tree.

    >>> pytunes = make_pytunes('i_love_t_swift')
    >>> num_songs(pytunes)
    3
    """
    "*** YOUR CODE HERE ***"

# Q3
def find(t, target):
    """Returns True if t contains a node with the value 'target' and False otherwise.

    >>> my_account = tree('kpop_king',
    ...                    [tree('korean',
    ...                          [tree('gangnam style'),
    ...                           tree('wedding dress')]),
    ...                     tree('pop',
    ...                           [tree('t-swift',
    ...                                [tree('blank space')]),
    ...                           tree('uptownfunk')])])
    >>> find(my_account, 'korean')
    True
    >>> find(my_account, 'blank space')
    True
    >>> find(my_account, 'bad blood')
    False
    """
    "*** YOUR CODE HERE ***"



# Q4
def delete(t, target):
    """Returns the tree that results from deleting target from t. If target is a category, 
    delete everything inside of it.

    >>> my_account = tree('kpop_king',
    ...                    [tree('korean',
    ...                          [tree('gangnam style'),
    ...                           tree('wedding dress')]),
    ...                     tree('pop',
    ...                           [tree('t-swift',
    ...                                [tree('blank space')]),
    ...                           tree('uptownfunk')])])
    >>> new = delete(my_account, 'pop')
    >>> print_tree(new)
    kpop_king
      korean
        gangnam style
        wedding dress
    """
    "*** YOUR CODE HERE ***"
	if entry(t) == target:
        return []
    if is_leaf(t):
        if entry(t) == target:
            return []
        else:
            return t
    else:
        new_branch = [delete(i,target) for i in subtrees(t)]
        new_branch = [x for x in new_branch if x != []]
    return tree(entry(t),new_branch)
   

# ADT
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