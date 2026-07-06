# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0 
        q = deque([(root,root.val)])
        cnt = 1 
        while q :
            l = len(q)
            for i in range(l):
                node,m = q.popleft()
                if node.left :
                    n = m 
                    if node.left.val >= n :
                        n = node.left.val 
                        cnt += 1
                    q.append((node.left,n))
                if node.right :
                    if node.right.val >= m :
                        m = node.right.val
                        cnt += 1
                    q.append((node.right,m))
        return cnt 