class Solution:
    def dfs(self,adj,visited,parent,node):
        visited[node] = True
        for i in adj[node]:
            if not visited[i]:
                parent[i] = node
                if(self.dfs(adj,visited,parent,i)):
                    return True
            elif(i != parent[node]):
                return True
        return False

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[]for _ in range(n)]
        visited = [False]*n
        parent = [-1]*n
        count = 0
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        for i in range(n):
            if(not visited[i]):
                cycle = self.dfs(adj,visited,parent,i)
                if(cycle == True):
                    return False
                count+=1

        if(count>1):
            return False
        else:
            return True
