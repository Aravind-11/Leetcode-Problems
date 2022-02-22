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
                print('a[5]')
            elif(i==10):
                if(a[5]==0):
                    return False
                else:
                    print('a[10]')
                    a[10]+=1
                    a[5]-=1
            else:
                print('here')
                print(a[10],a[5])
                if(a[10]>=1 and a[5]>=1):
                    print('1')
                    a[10]-=1
                    a[5]-=1
                    a[20]+=1
                    
                elif(a[10]==0 and a[5]>=3):
                    print('2')
                    a[20]+=1
                    a[5]-=3
                    
                else:
                    
                    print('3')
                    return False
                    
                    
                    
        return True 
                    
                
            
           
                
        