class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, height, visited):
            if (
                r < 0 or
                c < 0 or 
                r >= rows or 
                c >= cols or
                (r, c) in visited or
                heights[r][c] < height
            ):
                return

            visited.add((r, c))
            height = heights[r][c]

            dfs(r + 1, c, height, visited)
            dfs(r - 1, c, height, visited)
            dfs(r, c + 1, height, visited)
            dfs(r, c - 1, height, visited)

        res = []

        for c in range(cols):
            dfs(0, c, 0, pac)
            dfs(rows - 1, c, 0, atl)

        for r in range(cols):
            dfs(r, 0, 0, pac)
            dfs(r, cols - 1, 0, atl)

        for island in pac:
            if island in atl:
                res.append(list(island))

        return res

            

            