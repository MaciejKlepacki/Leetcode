class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        def DFS_visit(isConnected, u):
            visited[u] = True
            for v in range(len(isConnected[u])):
                if isConnected[u][v]==1 and not visited[v]:
                    DFS_visit(isConnected, v)

        for u in range(n):
            if not visited[u]:
                provinces += 1
                DFS_visit(isConnected, u)

        return provinces