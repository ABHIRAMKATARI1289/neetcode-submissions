class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h1 = defaultdict(int)
        for n in nums:
            h1[n] += 1
        
        freq = [[] for _ in range(len(nums) + 1)]

        for n,c in h1.items():
            freq[c].append(n)

        ans  = []
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k :
                    return ans 