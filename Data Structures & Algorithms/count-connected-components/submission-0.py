class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for nei in adjList[node]:
                dfs(nei)

        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)

        return res