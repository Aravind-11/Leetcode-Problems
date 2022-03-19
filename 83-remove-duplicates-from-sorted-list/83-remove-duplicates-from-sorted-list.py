# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        x=head
        head_s=None
        head_end=None
        while x:
            if not head_s:
                
                head_s=x
                head_end=head_s
            
                prev=x.val
            else:
                
                if x.val==prev:
                    
                    pass
                else:
                    
                    head_end.next=x
                    head_end=head_end.next
                    prev=x.val
            
            x=x.next
        head_end.next=None
        return head_s