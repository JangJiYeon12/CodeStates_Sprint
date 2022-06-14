def added_word(test_str1, test_str2):
    a = set(test_str1.split(' '))
    b = set(test_str2.split(' '))

    for i in b:
        if i not in a:
            return i

    return None
