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
    """return the height of a tree 树的深度没有想出好的方法（不只是2叉树）"""


def tree_size(tree):
    """return the size of a tree(the number of the nodes)"""
    num = 0
    for i in tree:
        if not is_tree(i):
            num += 1
        else:
            num += tree_size(i)
    return num

print(tree_size(t))

def tree_max(tree):
    """return the max of a tree 寻找树中最大的node"""
    num = 0
    for i in tree:
        if not is_tree(i):
            if i > num:
                num = i
        else:
            temp = tree_max(i)
            if num < temp:
                num = temp
    return num

print(tree_max(t))

t2 = tree(2,[tree(7,[tree(3),tree(6,[tree(5),tree(11)])]),tree(15)])

def find_path(tree,x):
    """ 寻找一个树从root到要找的数的path，如果没有，返回None
    >>>t = <see Above>
    >>>find_path(t,5)
    [2,7,6,5]
    >>>find_path(t,10)
    """
    for i in tree:
        if not is_tree(i):
            if i == x:
                return [root(tree)] + [i]
        else:
            if root(i) == x:
                return [root(tree)] + [root(i)]
    for i in tree:
        if is_tree(i):
            temp = find_path(i,x)
            if temp == None:
                continue
            else:
                return [root(tree)] + temp


print(find_path(t2,10))