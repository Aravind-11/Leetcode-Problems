class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        x=''
        for i in s:
            if(i.isalnum()):
                x+=i
        x=x.lower()
        
        return(x==x[::-1])
    
        