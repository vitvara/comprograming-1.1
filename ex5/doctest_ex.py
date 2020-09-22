def string_interleave(s1, s2):
    """[summary]

    Args:
        s1 (string): some word
        s2 (string): some word

    Returns:
        string: s1 swap with s2 or s2 swap with s1

    >>> string_interleave("abc", "mnopq")
    'manbocpq'
    >>> string_interleave("mnopq", "abc")
    'manbocpq'
    >>> string_interleave("Hello", "Sawasdee Thailand")
    'SHaewlalsodee Thailand'
    >>> string_interleave("Mine", "Thai")
    'TMhianie'
    """
    if len(s2) < len(s1):
        for i in range(len(s2)):
            s1 = s1[:2*i+1] + s2[i] + s1[2*i+1:]
        return s1
    else:
        for i in range(len(s1)):
            s2 = s2[:2*i+1] + s1[i] + s2[2*i+1:]
        return s2


def selective_sum(n, k):
    """[summary]

    Args:
        n (integer): number
        k (interger): select digit

    Returns:
        integer : sum of maxium digit

    Test:
    >>> selective_sum(3018, 2)
    11
    >>> selective_sum(593796, 3)
    25
    >>> selective_sum(12345, 10)
    15
    """
    list_ = []
    sum = 0
    if k > len(str(n)):
        return k + len(str(n))
    for i in str(n):
        list_.append(int(i))
    for i in range(k):
        sum += max(list_)
        list_.remove(max(list_))

    return sum


def list_intersect(l1, l2):
    """[summary]

    Args:
        l1 (list): list of number
        l2 (list): list of number

    Returns:
        list : list of number in l1 that intersect l2

    Test:
    >>> list_intersect([1, 2, 1, 3, 4], [1, 2, 2, 3, 4]) # return [1, 2, 3, 4]
    [1, 2, 3, 4]

    >>> list_intersect([1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8])
    [1, 2, 3, 4]
    >>> list_intersect([9, 10, 11, 12], [5, 6, 7, 8]) # return []
    []
    >>> list_intersect([9, 10, 11, 12], [5, 6, 9, 10, 7, 8]) # return [9, 10]
    [9, 10]
    """
    list_ = []
    for i in l1:
        for j in l2:
            if i == j:
                list_.append(i)

    return list(set(list_))


print(list_intersect([1, 2, 1, 3, 4], [1, 2, 2, 3, 4]))
