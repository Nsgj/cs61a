__author__ = 'computer'
def tree(value,branches = []):
    for branch in branches:
        assert is_tree(branch),'branches must be trees'
    return [value]+list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

t = tree(1,[tree(3,[tree(4),tree(5),tree(6)]),tree(2)])
print(t)
def square_tree(tree):
    root3 = []
    for i in tree:
        root1 = []
        root2 = []
        if not is_tree(i):
            root1 = [i * i]
        else:
            root2 = [square_tree(i)]
        root3 += root1 + root2
    return root3


def height(tree):
    """return the height of a tree"""
    n = 0
    for i in tree:
        if is_tree(i):
            n += 1
            height(i)
