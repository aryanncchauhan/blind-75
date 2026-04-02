class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += f"{len(word)}?{word}"
        
        print(res)

        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            sizeStr = ""
            while s[i] != "?":
                sizeStr += s[i]
                i += 1
                
            size = int(sizeStr)

            i += 1

            word = ""
            for _ in range(size):
                word += s[i]
                i += 1

            res.append(word)

        return res
