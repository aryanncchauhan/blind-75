class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     myMap = {}
    #     res = []

    #     # O(n)
    #     for num in nums:
    #         myMap[num] = myMap.get(num, 0) + 1

    #     # O(mlogm) where m is the number of unique keys
    #     myMapSorted = dict(sorted(myMap.items(), key=lambda x: x[1], reverse=True))

    #     # O(n)
    #     for num in myMapSorted:
    #         if len(res) < k:
    #             res.append(num)
    #         else:
    #             break
        
    #     return res

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for key, val in count.items():
            freq[val].append(key)

        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res