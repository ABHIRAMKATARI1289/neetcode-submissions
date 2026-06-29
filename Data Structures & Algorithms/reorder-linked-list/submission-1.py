# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        
        second = slow.next 
        slow.next = None
        
        before = None
        while second:
            after = second.next 
            second.next = before
            before = second 
            second = after 
            
        temp = head 
        while temp and before:
            next_temp = temp.next
            next_before = before.next
            temp.next = before
            before.next = next_temp
            before = next_before
            temp = next_temp
