class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums 
        
        res = []
        q = deque()

        for i,num in enumerate(nums):
            while q and q[-1] < num :
                q.pop()
            q.append(num)

            if i >= k and q[0] == nums[i-k] :
                q.popleft()
            
            if i >= k -1 :
                res.append(q[0])
        return res 

        