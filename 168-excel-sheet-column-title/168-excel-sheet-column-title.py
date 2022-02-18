class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        
        alpha='abcdefghijklmnopqrstuvwxyz'
        a={}
        for i in alpha.upper():
            a[ord(i)-64]=i
        
        #if(columnNumber<=26):
        #    return a[columnNumber]
        x=[]
        flag=0
        if(columnNumber<=26):
            return a[columnNumber]
        while(columnNumber>1):
            num1=columnNumber%26
            if(flag==1):
                
                num1-=1
                flag=0
                
            if(num1==0):
                flag=1
                num1=26
                
            
                
            #print('num1',num1)
            
            columnNumber=int(columnNumber/26)
            #print('c',columnNumber)
            
            x.insert(0,a[int(num1)])
            #print(x)
            
        if(columnNumber>=1 and flag!=1):
            #print('came here')
            x.insert(0,a[int(columnNumber)])
            
        return "".join(x)