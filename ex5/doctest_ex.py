def string_interleave(s1, s2):
    """
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


# def selective_sum(n, k):
print(string_interleave("abc", "mnopq"))
