# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        x=head
        h=head
        c=0
        while x:
            c+=1
            x=x.next
        if c==1:
            return 
        i=0
        if c-n==0:
            head=head.next
            return head
        while head:
            
            i+=1
            print i,c-n
            if i==c-n:
                temp=head.next
                head.next=temp.next
                
                break
            head=head.next
        return h
            