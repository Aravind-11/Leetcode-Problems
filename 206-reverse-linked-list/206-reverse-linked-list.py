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
        if not head:
            return 
        c=0
        head_copy=head
        while head_copy:
            c+=1
            head_copy=head_copy.next
        if c==1:
            return head
        p1=head.next
        head.next=None
        p2=p1.next
        while p1:
            print('1')
            p1.next=head
            head=p1
            p1=p2
            if p2:
                p2=p2.next
            else:
                return head
        
        