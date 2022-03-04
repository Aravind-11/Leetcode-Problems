# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 and not list2:
            return 
        if not list1:
            list1=list2
            return list1
        if not list2:
            return list1
        def insert_at_end(head,val):
            if not head:
                head=ListNode(val)
                return head
            itr=head
            while itr.next:
                itr=itr.next
            itr.next=ListNode(val)
            return head
        head=None
        c=[]
        while list1 and list2:
            if list1.val>list2.val:
                c.append(list2.val)
                list2=list2.next
            
            else:
                c.append(list1.val)
                list1=list1.next
        while list1:
            c.append(list1.val)
            list1=list1.next
        while list2:
            c.append(list2.val)
            list2=list2.next
        for i in c:
            
            head=insert_at_end(head,i)
        return head
                
        
        