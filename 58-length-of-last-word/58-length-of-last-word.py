class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(len(s)==1):
            return 1
        start=-1
        for i in range(len(s)-1,-1,-1):
            if(s[i]!=' '):
                end=i
                break
        for i in range(end,-1,-1):
            if(s[i]==' '):
                start=i
                break
        return end-start
        
            
        