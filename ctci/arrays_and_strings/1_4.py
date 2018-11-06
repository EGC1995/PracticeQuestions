def palindrome_perm(s):
    letters = dict()
    one_count = 0

    for letter in s:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    if len(s) %2 == 0:
        for key in letters:
            if letters[key]%2 != 0:
                return false
    else:
        for key in letters:
            if letters[key]%2 != 0:
                one_count += 1

    if one_count > 1:
        return False
    return True
    
