def num_even_digits(n):
    """
    >>> num_even_digits(223345)
    3
    >>> num_even_digits(973315)
    0
    >>> num_even_digits(88660022)
    8
    >>> num_even_digits(12345670)
    4
    """
    count = 0
    for i in str(n):
        if int(i) % 2 == 0:
            count += 1
    print(count)


def possible_rectangle(size1, size2, size3, size4):
    """
    >>> possible_rectangle(10, 20, 20, 10)
    True
    >>> possible_rectangle(10, 30, 20, 10)
    False
    >>> possible_rectangle(10, 10, 10, 10)
    True
    >>> possible_rectangle(10, 10, 20, 10)
    False
    """
    if size1 == size4 and size2 == size3:
        print(True)
        return None
    print(False)
