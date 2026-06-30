# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head 
        for _ in range(n):
            if fast is None :
                return None
            fast = fast.next
        Dummy = ListNode(0)
        slow = Dummy 
        slow.next = head 
        while fast :
            slow = slow.next 
            fast = fast.next 
        slow.next = slow.next.next 
        return Dummy.next 
        