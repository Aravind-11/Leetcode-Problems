# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head1=ListNode(0)
        y=head1
        x=head
        c=0
        while x:
            c+=1
            if c%2!=0:
                node=ListNode(x.val)
                head1.next=node
                head1=head1.next
            x=x.next
        x=head
        c=0
        while x:
            c+=1
            if c%2==0:
                node=ListNode(x.val)
                head1.next=node
                head1=head1.next
            x=x.next
        return y.next