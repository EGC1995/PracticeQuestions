def is_unique(s):
    letters = dict()
    for letter in s:
        if letter in letters:
            return False
        letters[letter] = 1
    return True
