class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if(s==s[::-1]):
            return True
        i,j=0,len(s)-1
        while(i<j):
            if(s[i]==s[j]):
                i+=1
                j-=1
            else:
                if(s[i+1:j+1]==s[i+1:j+1][::-1] or s[i:j]==s[i:j][::-1]):
                    return True
                else:
                    return False
        return False
        