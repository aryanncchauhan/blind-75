class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        inPacific, inAtlantic = set(), set()
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, height, ocean):
            if (
                r < 0 or
                c < 0 or 
                r >= rows or 
                c >= cols or
                heights[r][c] < height
            ):
                return

            if ocean == "pacific":
                if (r, c) in inPacific:
                    return
                else:
                    inPacific.add((r, c))
            elif ocean == "atlantic":
                if (r, c) in inAtlantic:
                    return
                else:
                    inAtlantic.add((r, c))

            height = heights[r][c]

            dfs(r + 1, c, height, ocean)
            dfs(r - 1, c, height, ocean)
            dfs(r, c + 1, height, ocean)
            dfs(r, c - 1, height, ocean)

        res = []

        for c in range(cols):
            dfs(0, c, 0, "pacific")
            dfs(rows - 1, c, 0, "atlantic")

        for r in range(cols):
            dfs(r, 0, 0, "pacific")
            dfs(r, cols - 1, 0, "atlantic")

        for island in inPacific:
            if island in inAtlantic:
                res.append(list(island))

        return res

            

            