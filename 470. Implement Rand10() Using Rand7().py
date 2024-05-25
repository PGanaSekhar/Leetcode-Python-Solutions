# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        curr = 40
        while curr >= 40:
            curr = (rand7() - 1) * 7 + rand7() - 1
        return curr % 10 + 1
