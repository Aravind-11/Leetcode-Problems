class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        
        a={}
        a[5]=0
        a[10]=0
        a[20]=0
        
        
        for i in bills:
            if(i==5):
                a[5]+=1
                
            elif(i==10):
                if(a[5]==0):
                    return False
                else:
                    a[10]+=1
                    a[5]-=1
            else:
                if(a[10]>=1 and a[5]>=1):
                    
                    a[10]-=1
                    a[5]-=1
                    a[20]+=1
                    
                elif(a[10]==0 and a[5]>=3):
                    
                    a[20]+=1
                    a[5]-=3
                    
                else:
                    
                
                    return False
                    
                    
                    
        return True 
                    
                
            
           
                
        