class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        a={}
        for i in set(t):
            a[i]=0
        for i in t:
            a[i]+=1
        for i in s:
            if i in s:
                a[i]-=1
        for i, j in enumerate(a):
            if(a[j]!=0):
                return j
        