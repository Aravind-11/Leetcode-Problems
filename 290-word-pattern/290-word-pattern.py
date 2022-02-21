class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        if(len(pattern)!=len(s.split(' '))):
            return False
        if(len(list(set(pattern)))!=len(list(set(s.split(' '))))):
            return False
        list1=s.split(' ')
        
        a={}
        list2=list(pattern)
        for i in range(len(list2)):
            #print(list2[i])
            a[list2[i]]=list1[i]
        arr=[]
        print(a)
        for i in pattern:
            arr.append(a[i])
            
        if(arr==s.split(' ')):
            return True
        
        
        