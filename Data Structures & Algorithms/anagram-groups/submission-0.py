class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for i in range(len(strs)):
            sortedWord = ''.join(sorted(strs[i]))
            if sortedWord in map:
                map[sortedWord].append(strs[i])
            else:
                map[sortedWord] = [strs[i]]
        return map.values()