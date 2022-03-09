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
            return
        a={}
        x=head
        while x:
            a[x.val]=0
            x=x.next
        x=head
        while x:
            a[x.val]+=1
            x=x.next
        y=None
        z=None
        x=head
        while x:
            if a[x.val]<2:
                if not y:
                    y=x
                    z=y
                else:
                    y.next=x
                    y=y.next
            x=x.next
        if not y:
            return 
        y.next=None
        return z