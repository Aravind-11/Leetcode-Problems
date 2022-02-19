class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
       
        c=0
        c1=len(s)
        s.sort()
        for i in g:
            flag=0
            j=0
            while(s and j<len(s)):
                
                if(s[j]>=i):
                    flag=1
                    break
                j+=1
            if(flag==1):
                c+=1
                del s[j]
                
        return c
        