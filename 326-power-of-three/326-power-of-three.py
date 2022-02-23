class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if not n :return False
        
        if n==1:
            return True
        if(n%3!=0):
            return False
        if n<1:
            return False
        
        
        return self.isPowerOfThree(n//3)
        
        