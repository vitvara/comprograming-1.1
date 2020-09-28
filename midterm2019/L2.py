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
