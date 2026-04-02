class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}

        for word in strs:
            sorted_word = sorted(word)
            sorted_word = "".join(sorted_word)

            if sorted_word not in hash:
                hash[sorted_word] = []
            
            hash[sorted_word].append(word)

        res = []

        for words in hash.values():
            res.append(words)

        return res