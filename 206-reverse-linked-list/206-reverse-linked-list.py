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
        c=[]
        x=head
        while x:
            c.append(x.val)
            x=x.next
        x=head
        c=c[::-1]
        for i in c:
            x.val=i
            x=x.next
            if not x:
                return head
        
        