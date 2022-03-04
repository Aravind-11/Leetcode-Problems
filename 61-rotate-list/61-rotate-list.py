# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        c=0
        x=head
        while x:
            c+=1
            x=x.next
        #print c
        if not c:
            return
        if c==1:
            return head
        
        k=k%c
        if not k:
            return head
        i=0
        x=head
        while x:
            i+=1
            if i==c-k+1:
                p1=x
                p_val=x
            
                break
            x=x.next
        y=p1
        
        while p1.next:
            
            p1=p1.next
        p1.next=head
        
        x=head
        while x.next:
            if x.next==p_val:
                #print p_val
                x.next=None
                break
                
            x=x.next
        return y
        