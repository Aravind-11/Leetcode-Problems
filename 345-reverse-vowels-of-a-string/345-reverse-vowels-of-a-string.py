class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        v='aeiouAEIOU'
        i,j=0,len(s)-1
        while i<j:
            if s[i] not in v:
                i+=1
            elif s[j] not in v:
                j-=1
            elif s[i] in v and s[j] in v:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        return "".join(s)
                
        