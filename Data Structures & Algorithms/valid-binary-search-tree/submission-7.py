# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool: 
        q = deque([(root,[float('-inf'),float('inf')])])
        while q :
            l = len(q)
            for i in range(l):
                node,bound = q.popleft()
                if node.left:
                    band = bound.copy()
                    if node.left.val >= node.val or node.left.val >= band[1] or node.left.val <= band[0]:
                        return False 
                    band[1] = node.val
                    q.append((node.left,band))
                if node.right :
                    band2 = bound.copy()
                    if node.right.val <= node.val or node.right.val <= band2[0] or node.right.val >= band2[1]:
                        return False 
                    band2[0] = node.val
                    q.append((node.right,band2))
        return True 
        