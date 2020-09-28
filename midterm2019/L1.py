def group_elements(l):
    """
    >>> group_elements([1, 3, 3, 4, 2, 5, 8, 5, 6, 7])
    [[1], [3, 3], [4], [2], [5, 5], [8], [6], [7]]
    >>> group_elements([3, 3, 3, 3])
    [[3, 3, 3, 3]]
    >>> group_elements([3, 3, 1, 3, 3, 1])
    [[3, 3, 3, 3], [1, 1]]
    >>> group_elements([5, 3, 1, 2, 4, 10])
    [[5], [3], [1], [2], [4], [10]]
    """
    local_list = []
    return_list = []
    used_num = []
    for i in l:
        if i not in used_num:
            for j in range(len(l)):
                if i == l[j]:
                    local_list.append(i)
            return_list.append(local_list)
            local_list = []
            used_num.append(i)

    print(return_list)


group_elements([5, 3, 1, 2, 4, 10])
