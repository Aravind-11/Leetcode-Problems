class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        
        columnnumber=[]
        for i in range(len(columnTitle)):
            columnnumber.append(26**(i))
    
        for i in range(len(columnTitle)-1,-1,-1):
            columnnumber[i]=columnnumber[i]+(26**(len(columnTitle)-1-i)*(ord(columnTitle[i])-ord('A')))
        return sum(columnnumber)
            
        