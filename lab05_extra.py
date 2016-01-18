from lab05 import *

## Extra Lists, Dictionaries Questions ##

#########
# Lists #
#########

# Q12
def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
    result = []
    if lst1 == [] or lst2 == []:
        result = lst1 + lst2
        return result
    elif lst1[0] > lst2[0]:
        result.append(lst2[0])
        result +=  merge(lst1,lst2[1:])
    else:
        result.append(lst1[0])
        result += merge(lst1[1:],lst2)
    return result

# Q13
def mergesort(seq):
    """Mergesort algorithm.

    >>> mergesort([4, 2, 5, 2, 1])
    [1, 2, 2, 4, 5]
    >>> mergesort([])     # sorting an empty list
    []
    >>> mergesort([1])   # sorting a one-element list
    [1]
    """
	"""不使用递归的算法：
	依次用2个组成的段，遍历形成新的seq，再用4个组成的段遍历，以此类推，最后只有一个段"""
    #首先遍历单个元素
    length = len(seq)
    if length == 0:
        return []
    
    re = []
    n = 0
    while n < length:
        if n + 1 == length:
            re += merge([seq[n]],[])
        else:
            re += merge([seq[n]],[seq[n + 1]])
        n += 2
    seq = re
    #再遍历2个和多个组成的一段元素
    i = 2
    while True:
        re = []
        n = 0
        while n + 2 * i < length:
            re += merge(seq[n:n + i],seq[n + i:n + 2 * i])
            n += 2 * i
        re += merge(seq[n:n + i],seq[n + i:])
        seq = re
        if i >= length:
            return seq
        i *= 2

# Q14
def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> fn = lambda x: x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """ 
    "*** YOUR CODE HERE ***"
    return [[x,fn(x)] for x in seq if fn(x) >= lower and fn(x) <= upper]


# Q15
def deck(suits, numbers):
    """Creates a deck of cards (a list of 2-element lists) with the given
    suits and numbers. Each element in the returned list should be of the form
    [suit, number].

    >>> deck(['S', 'C'], [1, 2, 3])
    [['S', 1], ['S', 2], ['S', 3], ['C', 1], ['C', 2], ['C', 3]]
    >>> deck(['S', 'C'], [3, 2, 1])
    [['S', 3], ['S', 2], ['S', 1], ['C', 3], ['C', 2], ['C', 1]]
    >>> deck([], [3, 2, 1])
    []
    >>> deck(['S', 'C'], [])
    []
    """
    "*** YOUR CODE HERE ***"
    return [[x,y] for x in suits for y in numbers]


################
# Dictionaries #
################

# Q16
def counter(message):
    """ Returns a dictionary of each word in message mapped
    to the number of times it appears in the input string.

    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    word_list = message.split()
    "*** YOUR CODE HERE ***"
    dic = {}
    for i in word_list:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic

# Q17
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
