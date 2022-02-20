class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        
        columnnumber=[]
        for i in range(len(columnTitle)):
            columnnumber.append(26**(i))
        columnTitle=columnTitle[::-1]
        for i in range(len(columnTitle)):
            columnnumber[i]=columnnumber[i]+(26**i*(ord(columnTitle[i])-ord('A')))
        return sum(columnnumber)
            
        