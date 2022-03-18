class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==1:
            return s
        c=[]
        for i in s:
            
            if len(c)!=0:
                
                
                if i.islower():
                    
                    if c[-1]==i.upper():
                        
                        c.pop()
                    else:
                    
                        c.append(i)
                elif i.isupper():
                    
                    if c[-1]==i.lower():
                        
                        c.pop()
                    else:
                    
                        c.append(i)
                
                
            else:
                c.append(i)
            
        return ''.join(c)