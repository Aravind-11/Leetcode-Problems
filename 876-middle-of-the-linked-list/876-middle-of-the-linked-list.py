# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        c=0
        x=head
        while x:
            c+=1
            x=x.next
        
        m=c//2
        i=0
        
        while head:
            i+=1
            if i==m+1:
                return head
                
            head=head.next
            
        