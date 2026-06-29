# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        temp = res
        l1 = list1
        l2 = list2
        while l1  and l2:
            if l1.val < l2.val:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            else :
                temp.next = ListNode(l2.val)
                l2 = l2.next 
            temp = temp.next 
        if l1 :
            temp.next = l1
        if l2 :
            temp.next = l2
            
        return res.next
