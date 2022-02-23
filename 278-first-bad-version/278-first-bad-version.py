# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,h=1,n
        index=-1
        while l<=h:
            
            m=(l+h)//2
            
            if isBadVersion(m):
                index=m
                h=m-1
            else:
                l=m+1
        return index
        