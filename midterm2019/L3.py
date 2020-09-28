def string_union(str1, str2):
    """
    >>> string_union("abcde", "abcwxyz")
    'abcdewxyz'
    >>> string_union("abcde", "wxyz")
    'abcdewxyz'
    >>> string_union("abcde", "wxyabzc")
    'abcdewxyz'
    """
    local_list = []
    return_str = ""
    for i in list(str1):
        local_list.append(i)
    for i in list(str2):
        local_list.append(i)
    return_list = list(set(set(local_list)))
    return_list.sort()
    for i in return_list:
        return_str += i

    print(f"'{return_str}'")


def string_intersect(str1, str2):
    """
    >>> string_intersect("abcde", "abcwxyz")
    'abc'
    >>> string_intersect("abcde", "wxyz")
    ''
    >>> string_intersect("abcde", "wxyabzc")
    'abc'
    """
    return_list = []
    for i in str1:
        if i in str2:
            return_list.append(i)
    return_str = ""
    for i in return_list:
        return_str += i
    print(f"'{return_str}'")
