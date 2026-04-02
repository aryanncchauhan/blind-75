class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs)):
            res += str(len(strs[i])) + "#" + strs[i]
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            count = ""
            while s[i] != "#":
                count += s[i]
                i += 1
            num = int(count)
            i += 1
            word = ""
            for j in range(num):
                word += s[i]
                i += 1
            res.append(word)
        return res