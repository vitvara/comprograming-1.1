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
