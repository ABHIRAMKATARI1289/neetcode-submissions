class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        h1 = {}

        for n in nums :
            h1[n] = h1.get(n,0) + 1  
        
        for key,val in h1.items():
            heapq.heappush(heap,(-val,key))
        
        res = []
        while len(res) < k :
            res.append(heapq.heappop(heap)[1])
        
        return res 
