class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        a={i:0 for i in s}
        for i in s:
            a[i]+=1
        count=0
        oddFound=False
        for i,j in enumerate(a):
            if(a[j]%2==0):
                count+=a[j]
            else:
                count+=a[j]-1
                oddFound=True
        return count+1 if oddFound else count
                
       
                
            
        
        