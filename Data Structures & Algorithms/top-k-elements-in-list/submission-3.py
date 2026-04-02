class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        res = []

        for num in nums:
            myMap[num] = myMap.get(num, 0) + 1

        myMapSorted = dict(sorted(myMap.items(), key=lambda x: x[1], reverse=True))

        for num in myMapSorted:
            if len(res) < k:
                res.append(num)
            else:
                break
        
        return res
        