# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c1=c2=''
        while l1:
            c1+=str(l1.val)
            l1=l1.next
        while l2:
            c2+=str(l2.val)
            l2=l2.next
        c1=c1[::-1]
        c2=c2[::-1]
        c3=list(str(int(c1)+int(c2)))
        c3=c3[::-1]
        for i in range(len(c3)):
            c3[i]=int(c3[i])
        head=ListNode(c3[0])
        x=head
        for i in range(1,len(c3)):
            head.next=ListNode(c3[i])
            head=head.next
        return x