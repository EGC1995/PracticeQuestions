# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # seem like the 'trick' here is to read the string backwards
        digits = list(s)
        index = len(digits) - 1
        finalValue = 0
        while(index >= 0):
            if(value(digits[index]) > (digits[index - 1]))

#helper function
def value(x):
    if(x == "I"):
        return 1
    elif(x == "V"):
        return 5
    elif(x == "X"):
        return 10
    elif(x == "L"):
        return 50
    elif(x == "C"):
        return 100
    elif(x == "D"):
        return 500
    elif(x == "M"):
        return 1000
    return 0
