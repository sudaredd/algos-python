def one_edit(str1, str2):
    if len(str2) > len(str1):
        return one_edit(str2, str1)

    pos1, pos2 = 0, 0

    if len(str1) - len(str2) > 1:
        return False
    saw_diff = False
    while pos1 < len(str1) and pos2 < len(str1):
        if str1[pos1] != str2[pos2]:
            if saw_diff:
                return False
            saw_diff = True
            if len(str1) > len(str2):
                pos1 = pos1 + 1
                continue
        pos1 = pos1 + 1
        pos2 = pos2 + 1
    return True


# print(one_edit('cat', 'cat'))
print(one_edit('cat', 'can'))
print(one_edit('cbat', 'cct'))
