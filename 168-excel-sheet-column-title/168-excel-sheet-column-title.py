class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        
        ans=''
    
        while True:
            columnNumber-=1
            rem=columnNumber%26
            columnNumber//=26
            ans+=chr(rem+ord('A'))
            if(columnNumber==0):
                return ans[::-1]