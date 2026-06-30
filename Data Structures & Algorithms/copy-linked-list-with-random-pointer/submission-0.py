"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head :
            return None
        hash1 = {}
        temp = head 
        while temp :
            hash1[temp] = Node(temp.val)
            temp = temp.next 
        
        curr = head 
        while curr :
            hash1[curr].next = hash1.get(curr.next) 
            hash1[curr].random = hash1.get(curr.random) 
            curr = curr.next 
        return hash1[head]

        