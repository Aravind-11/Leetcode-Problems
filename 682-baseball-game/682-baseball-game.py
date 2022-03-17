class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        c=[]
        flag=-1
        for i in range(len(ops)):
            
            if ops[i]=='C':
                c.pop()
                
            elif ops[i]=='+':
                x=c.pop()
                y=c.pop()
                c.append(y)
                c.append(x)
                c.append(x+y)
        
            elif ops[i]=='D':
                z=c.pop()
                c.append(z)
                c.append(2*z)
            
            else:
                c.append(int(ops[i]))
        return sum(c)