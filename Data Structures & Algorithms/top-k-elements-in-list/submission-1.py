import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1

        pq = []
        for num in map.keys():
            heapq.heappush(pq, (-1 * map[num], num))

        res = []
        
        for i in range(k):
            res.append(heapq.heappop(pq)[1])

        return res

        
        