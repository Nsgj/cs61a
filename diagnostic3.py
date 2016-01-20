__author__ = 'computer'
# Linked List definition
empty = 'empty'

def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (type(s) == list and len(s) == 2 and is_link(s[1]))

def link(first, rest=empty):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), 'rest must be a linked list.'
    return [first, rest]

def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), 'first only applies to linked lists.'
    assert s != empty, 'empty linked list has no first element.'
    return s[0]

def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), 'rest only applies to linked lists.'
    assert s != empty, 'empty linked list has no rest.'
    return s[1]

def print_link(s):
    """Print elements of a linked list s.

    >>> s = link(1, link(2, link(3, empty)))
    >>> print_link(s)
    1 2 3
    """
    line = ''
    while s != empty:
        if line:
            line += ' '
        line += str(first(s))
        s = rest(s)
    print(line)


def if_this_not_that(i_list,this):
    """
    >>> original_list = [1, 2, 3, 4, 5]
    >>> if_this_not_that(original_list, 3)
    that
    that
    that
    4
    5
    """
    for i in i_list:
        if i > this:
            print(i)
        else:
            print('that')

def group(seq):
    """Divide a sequence of at least 12 elements into groups of 4 or
    5. Groups of 5 will be at the end. Returns a list of sequences, each
    corresponding to a group.

    >>> group(range(14))
    [range(0, 4), range(4, 9), range(9, 14)]
    >>> group(list(range(17)))
    [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15, 16]]
    """
    num = len(seq)
    assert num >= 12
    "*** YOUR CODE HERE ***"
    def help(seq):
        num = len(seq)
        if num == 0:
            return []
        if num % 4 == 0:
            return [seq[:4]] + help(seq[4:])
        else:
            return help(seq[:num - 5]) + [seq[num - 5:]]

    return help(seq)
def apply_to_all(map_fn, s):
        return [map_fn(x) for x in s]

def keep_if(filter_fn, s):
        return [x for x in s if filter_fn(x)]

def reduce(reduce_fn, s, initial):
        reduced = initial
        for x in s:
            reduced = reduce_fn(reduced, x)
        return reduced
"""
>>> apply_to_all(_______, [1, 3, -1, -4, 2])
[1, 1, -1, -1, 1]
>>> keep_if(______, [1, 7, 14, 21, 28, 35, 42])
[1, 14, 28, 42]
>>> reduce(_______, _______, '')
'olleh'
>>> reduce(______, apply_to_all(______, 'nnnnn'), __) + ' batman!'
'nanananana batman!'
"""
print(apply_to_all(lambda x : x // abs(x),[1, 3, -1, -4, 2]))
print(keep_if(lambda x : (x // 7) % 2 == 0,[1, 7, 14, 21, 28, 35, 42]))
print(reduce(lambda x,y:x + y, 'elleh', ''))
print(reduce(lambda x,y:x + y,apply_to_all(lambda x:x+'a','nnnnn'),'') + ' batman!')

def replace_all(d, x, y):
    """
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> replace_all(d, 3, 'poof')

    >>> d == {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    "*** YOUR CODE HERE ***"
    for i in d:
        if d[i] == x:
            d[i] = y

def filter_link(predicate, r):
    """ Returns a link only containing elements in r that satisfy
    predicate.

    """
    "*** YOUR CODE HERE ***"
    if r == 'empty':
        return 'empty'
    if predicate(first(r)):
        return link(first(r),filter_link(predicate,rest(r)))
    else:
        return filter_link(predicate,rest(r))

r = link(25, link(5, link(50, link(49, empty))))
new = filter_link(lambda x : x % 2 == 0, r)
print(first(new))
print(rest(new) == 'empty')

"""重点在，选择first为一个点，将后面的放到它的前面"""
def reverse_iterative(s):
    """Return a reversed version of a linked list s.

    """
    "*** YOUR CODE HERE ***"
    end = link(first(s))
    done = rest(s)
    while done != 'empty':
        fir = first(done)
        end = link(fir,end)

        done = rest(done)

    return end

primes = link(2, link(3, link(5, link(7, empty))))

def reverse_recursive(s):

    end = link(first(s))

    def help(s):
        nonlocal end
        if s == 'empty':
            return
        end = link(first(s),end)
        help(rest(s))
    help(rest(s))
    return end

print(reverse_recursive(primes))