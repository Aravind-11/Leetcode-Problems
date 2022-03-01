class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        
        max_pos=-1
        i,j=0,len(num)-1
        while i<=j:
            if int(num[j])%2!=0:
                max_pos=j
                break
                    
            else:
                j-=1
                
                
        return num[i:max_pos+1]