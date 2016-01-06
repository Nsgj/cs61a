def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)
def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        i = 4
        a,b,c = 1,2,3
        while i <= n:
            a,b,c = b,c,3 * a + 2 * b + c
            i += 1
        return c

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    "*** YOUR CODE HERE ***"
    def help(i,a=1,b=-1,r=1):
        if i == n:
            return r
        elif has_seven(i) or i % 7 == 0:
            return help(i + 1,b,a,r + b)
        else:
            return help(i + 1,a,b,r + a)
    return help(1)


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)


def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    def count(n,m):
        if n < 0:
            return 0
        if n == 0:
            return 1
        if m > amount:
            return 0
        with_m = count(n - m,m)
        without_m = count(n,m * 2)
        return with_m + without_m
    return count(amount,1)

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    def help(n,s,d,t):
        if n == 1:
            print_move(s,d)
            return 0
        if help(n-1,s,t,d) == 0:
            print_move(s,d)
            return help(n-1,t,d,s)
    if start != 3 and end != 3:
        t = 3
    elif start != 1 and end != 1:
        t = 1
    elif start != 2 and end != 2:
        t = 2    
    help(n,start,end,t)

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.
	g0 = lambda self,n: 1 if n == 0 else n * self(self,n - 1)
	g0(g0,5)
	
	g1 = lambda self:lambda n: 1 if n == 0 else n * self(self,n - 1)
	g1(g1)(5)
	
	
    y算子的应用（匿名递归函数）
	y = lambda f:(lambda x:f(lambda y:x(x)(y)))(lambda x:f(lambda y:x(x)(y)))
	g = lambda f:lambda n:1 if n == 0 else n * f(n - 1)
	y(g)(5)
	
    >>> make_anonymous_factorial()(5)
    120
    """
    return (lambda f:(lambda x:f(lambda y:x(x)(y)))(lambda x:f(lambda y:x(x)(y))))(lambda g:lambda n:1 if n==0 else n*g(n - 1))

