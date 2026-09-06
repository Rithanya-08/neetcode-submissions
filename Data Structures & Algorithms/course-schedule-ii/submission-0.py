class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        adj = [[] for _ in range(numCourses)]
        queue = []

        for i,j in prerequisites:
            adj[j].append(i)
            indegree[i] += 1

        for k in range(numCourses):
            if(indegree[k] == 0):
                queue.append(k)

        result = []

        while(queue):
            ele = queue.pop(0)
            result.append(ele)

            for p in adj[ele]:
                indegree[p] -= 1
                if(indegree[p] == 0):
                    queue.append(p)

        if(numCourses == len(result)):
            return result
        else:
            return []
        


        