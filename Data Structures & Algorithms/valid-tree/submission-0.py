class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False

        adjList = [[] for _ in range(n)]

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = set()

        def dfs(node, par):
            if node in visited:
                return False

            visited.add(node)

            for nei in adjList[node]:
                if nei == par:
                    continue
                elif not dfs(nei, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n