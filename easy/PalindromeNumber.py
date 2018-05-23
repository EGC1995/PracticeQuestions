# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        index = 0
        if(x < 0):
            return False
        elif(x < 10):
            return True
        else:
            digits = list(str(x)) # note split() doesn't work
            endindex = len(digits)-1
            while(index != endindex and index < endindex):
                if(digits[index] == digits[endindex]):
                    index = index + 1
                    endindex = endindex - 1
                else:
                    return False
            return True
