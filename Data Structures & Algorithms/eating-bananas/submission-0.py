class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canfinish(k):
            return sum((p+k-1)//k for p in piles) <= h 
        
        l = 1 
        r = max(piles)
        ans = r
        while l <= r :
            mid = l + (r-l)//2

            if canfinish(mid):
                ans = mid 
                r = mid - 1 
            else :
                l = mid + 1 
        return ans 
