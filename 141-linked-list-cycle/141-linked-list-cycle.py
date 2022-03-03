# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        x=head
        s=set()
        while x:
            if x in s:
                return True
            s.add(x)
            x=x.next
        return False