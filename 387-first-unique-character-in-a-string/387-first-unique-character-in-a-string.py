class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        a={}
        for i in set(s):
            a[i]=0
        for i in s:
            a[i]+=1
        for i in range(len(s)):
            if(a[s[i]]==1):
                return i
        return -1