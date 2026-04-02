class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash = {}

        # # list iteration = O(n)
        # for word in strs:
        #     # sorting = O(mlog(m))
        #     sorted_word = sorted(word)

        #     # join = O(m)
        #     sorted_word = "".join(sorted_word)

        #     # hash operation = O(1)
        #     if sorted_word not in hash:
        #         hash[sorted_word] = []
            
        #     hash[sorted_word].append(word)

        # res = []

        # # list iteration = O(n)
        # for words in hash.values():
        #     res.append(words)

        # return res

# tc = O(n) * O(mlog(m)) = O(nmlog(m))
# n = length of strs list
# m = length of longest string

        hash = defaultdict(list)

        # iterate list = O(n)
        for s in strs:
            count = [0] * 26

            # iterate word = O(n)
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            hash[tuple(count)].append(s)

        return list(hash.values())

# tc = O(n) * O(m) = O(nm)
# n = length of strs list
# m = length of longest string