# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        
        while head:
            if head.val==val:
                head=head.next
            else:
                break
        if not head:
            return
        x=head
        if not x.next:
            if x.val==val:
                head=None
                return
        while x.next:
            if x.val==val:
                x.val=x.next.val
                x.next=x.next.next
            else:
                x=x.next
        y=head
        while y.next:
            if y.next.val==val:
                y.next=None
            else:
                y=y.next
        
        
        
            
        return head