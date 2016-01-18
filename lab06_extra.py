from lab06 import *

## Linked Lists ##

#Q5

def has_prefix(s, prefix):
    """Returns whether prefix appears at the beginning of linked list s.

    >>> x = link(3, link(4, link(6, link(6))))
    >>> print_link(x)
    3 4 6 6
    >>> has_prefix(x, empty)
    True
    >>> has_prefix(x, link(3))
    True
    >>> has_prefix(x, link(4))
    False
    >>> has_prefix(x, link(3, link(4)))
    True
    >>> has_prefix(x, link(3, link(3)))
    False
    >>> has_prefix(x, x)
    True
    >>> has_prefix(link(2), link(2, link(3)))
    False
    """
    "*** YOUR CODE HERE ***"
    if len_link(s) < len_link(prefix):
        return False
    if prefix == 'empty':
        return True
    if first(s) == first(prefix):
        return has_prefix(rest(s),rest(prefix))
    else:
        return False

def has_sublist(s, sublist):
    """Returns whether sublist appears somewhere within linked list s.

    >>> has_sublist(empty, empty)
    True
    >>> aca = link('A', link('C', link('A')))
    >>> x = link('G', link('A', link('T', link('T', aca))))
    >>> print_link(x)
    G A T T A C A
    >>> has_sublist(x, empty)
    True
    >>> has_sublist(x, link(2, link(3)))
    False
    >>> has_sublist(x, link('G', link('T')))
    False
    >>> has_sublist(x, link('A', link('T', link('T'))))
    True
    >>> has_sublist(link(1, link(2, link(3))), link(2))
    True
    >>> has_sublist(x, link('A', x))
    False
    """
    "*** YOUR CODE HERE ***"
    if sublist == 'empty':
        return True
    if len_link(s) < len_link(sublist):
        return False
    if has_prefix(s,sublist):
        return True
    else:
        return has_sublist(rest(s),sublist) 
def has_61A_gene(dna):
    """Returns whether linked list dna contains the CATCAT gene.

    >>> dna = link('C', link('A', link('T')))
    >>> dna = link('C', link('A', link('T', link('G', dna))))
    >>> print_link(dna)
    C A T G C A T
    >>> has_61A_gene(dna)
    False
    >>> end = link('T', link('C', link('A', link('T', link('G')))))
    >>> dna = link('G', link('T', link('A', link('C', link('A', end)))))
    >>> print_link(dna)
    G T A C A T C A T G
    >>> has_61A_gene(dna)
    True
    >>> has_61A_gene(end)
    False
    """
    "*** YOUR CODE HERE ***"
    gen = link('C',link('A',link('T',link('C',link('A')))))
    return has_sublist(dna,gen)

#Q6

def count_change(amount, denominations):
    """Returns the number of ways to make change for amount.

    >>> denominations = link(50, link(25, link(10, link(5, link(1)))))
    >>> print_link(denominations)
    50 25 10 5 1
    >>> count_change(7, denominations)
    2
    >>> count_change(100, denominations)
    292
    >>> denominations = link(16, link(8, link(4, link(2, link(1)))))
    >>> print_link(denominations)
    16 8 4 2 1
    >>> count_change(7, denominations)
    6
    >>> count_change(10, denominations)
    14
    >>> count_change(20, denominations)
    60
    """
    "*** YOUR CODE HERE ***"
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if denominations == 'empty':
        return 0
    with_f = count_change(amount - first(denominations),denominations)
    without_f = count_change(amount,rest(denominations))
    return with_f + without_f
