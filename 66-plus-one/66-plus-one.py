class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        x=''
        for i in digits:
            x+=str(i)
        x=int(x)+1
        x=str(x)
        list1=[]
        for i in x:
            list1.append(int(i))
        return list1