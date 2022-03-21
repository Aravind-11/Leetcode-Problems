# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        temp1=head.next
        head.next=None
        while temp1:
            temp2=temp1.next
            temp1.next=head
            head=temp1
            temp1=temp2
            if not temp1:
                break
        return head
        
        