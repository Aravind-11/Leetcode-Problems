# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getMid(self,head):
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def mergeSort(self,list1,list2):
        temp=dummy=ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                temp.next=list1
                list1=list1.next
            else:
                temp.next=list2
                list2=list2.next
            temp=temp.next
        if list1:
            temp.next=list1
        if list2:
            temp.next=list2
        return dummy.next
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        left=head
        right=self.getMid(head)
        temp=right.next
        right.next=None
        right=temp
        
        left=self.sortList(left)
        right=self.sortList(right)
        
        return self.mergeSort(left,right)
    
    
        