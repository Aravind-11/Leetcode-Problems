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
            if(a[j]%2==0): # if frequency is even, then it can be made into a palindrome
                count+=a[j] 
            else:
                count+=a[j]-1 # if frequency is odd, we remove one element from the freque
                oddFound=True
        return count+1 if oddFound else count 
    # if odd is found , then take that one element
                
       
                
            
        
        