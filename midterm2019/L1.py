def all_equal_int(x1, x2, x3, x4):
    """
    >>> all_equal_int(3, 3, 3, 3)
    True
    >>> all_equal_int(3, 2, 2, 3)
    False
    >>> all_equal_int(3, 2, 2, 2)
    False
    >>> all_equal_int(3, 3, 3, 2)
    False
    """
    l = [x1, x2, x3, x4]
    for i in l:
        for j in l:
            if i != j:
                print(False)
                return None
    print(True)


def circles_overlapping(x1, y1, x2, y2, r):
    """
    >>> circles_overlapping(0, 0, 2, 0, 2)
    True
    >>> circles_overlapping(2, 2, 4, 2, 0.7)
    False
    >>> circles_overlapping(1, 1, 2, 2, 0.6)
    False
    >>> circles_overlapping(1, 1, 4, 5, 3)
    True
    """
    distance = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
    if (distance/2) <= r:
        print(True)
        return None
    print(False)


circles_overlapping(1, 1, 4, 5, 3)
