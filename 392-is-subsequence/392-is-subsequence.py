class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        x=''
        prev=-1
        first=0
        for i in range(len(t)):
            if first<len(s) and s[first]==t[i] and i>prev:
                x+=s[first]
                first+=1
                prev=i
        if(x==s):
            return True
        return False
            
        