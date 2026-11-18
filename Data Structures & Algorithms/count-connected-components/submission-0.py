class Solution:
    def dfs(self,adj,visited,node):
        visited[node] = True

        for x in adj[node]:
            if not visited[x]:
                self.dfs(adj,visited,x)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False]*n
        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        count = 0
        for i in range(n):
            if(visited[i] == False):
                self.dfs(adj,visited,i)
                count = count+1

        return count
