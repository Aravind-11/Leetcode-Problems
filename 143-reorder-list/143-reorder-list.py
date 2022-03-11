# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
    
            return head
        
        
        def reverse_list(head1):
            temp=head1.next
            temp1=temp.next
            head1.next=None
            while temp:
                temp1=temp.next
                temp.next=head1
                head1=temp
                temp=temp1
                
            return head1
        x=head
        n=0
        
        while x:
            n+=1
            x=x.next
        
        x=head
        count=0
        
        while x:
            count+=1
            if count==n//2:
                
                tail=reverse_list(x.next)
                x.next=None
                break
            x=x.next
        x=head
        y=tail
        p_start=p_end=None
        while x:
            if not p_start:
                p_start=x
                p_end=p_start
                
            else:
                p_end.next=y
                p_end=p_end.next
                y=y.next
                p_end.next=x
                p_end=p_end.next
            
            if not x.next:
                    
                    x.next=y
                    
                    break
            
            x=x.next
        
        return head
                
            
            
        