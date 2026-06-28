class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h1 = defaultdict(int)
        for n in nums:
            h1[n] += 1

        res = []
        for num,cnt in h1.items():
            res.append([cnt,num])
        res.sort()

        ans = []
        for cnt,num in res[-k:]:
            ans.append(num)
        return ans 