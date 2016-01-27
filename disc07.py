def square_elements(lst):
    """
>>> lst = [1, 2, 3]
>>> square_elements(lst)
>>> lst
[1, 4, 9]
"""
    for i in range(len(lst)):
        lst[i] = lst[i] * lst[i]

def remove_all(el, lst):
    """
>>> x = [3, 1, 2, 1, 5, 1, 1, 7]
>>> remove_all(1, x)
>>> x
[3, 2, 5, 7]
"""
    while el in lst:
        lst.remove(el)

def reverse(lst):
    """ Reverses lst in place.
>>> x = [3, 2, 4, 5, 1]
>>> reverse(x)
>>> x
[1, 5, 4, 2, 3]
"""
    length = len(lst)
    n = 1
    while n < length:
        lst.insert(0,lst[n])
        del lst[n + 1]
        n += 1

def add_this_many(x, el, lst):
    """ Adds el to the end of lst the number of times x occurs
in lst.
>>> lst = [1, 2, 4, 2, 1]
>>> add_this_many(1, 5, lst)
>>> lst
[1, 2, 4, 2, 1, 5, 5]
"""
    while x >= 0:
        lst.append(el)
		x -= 1