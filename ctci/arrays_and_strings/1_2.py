def check_perm(s, t):
    if(len(s) != len(t)):
        return false
    letters = dict()

    for letter in s:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    for letter in t:
        if letter in letters:
            letters[letter] -= 1
        else:
            return False

    for key in letters:
        if !letters[key]:
            return False
    return True
