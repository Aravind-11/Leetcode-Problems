# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        c1=c2=0
        
        x=headA
        y=headB
        
        while x:
            c1+=1
            x=x.next
        while y:
            c2+=1
            y=y.next
        x=headA
        y=headB
        if c1>c2:
            while x:
                
                if c1==c2:
                    break
                c1-=1
                x=x.next
        else:
            while y:
                
                if c1==c2:
                    break
                c2-=1
                y=y.next
        while x and y:
            if x==y:
                return x
            x=x.next
            y=y.next
        return 
        
        
            