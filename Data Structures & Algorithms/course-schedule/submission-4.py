class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        adj = [[] for _ in range(numCourses)]
        queue = []

        for i,j in prerequisites:
            adj[i].append(j)
            indegree[j] += 1

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

        print(result)
        if(numCourses == len(result)):
            return True
        else:
            return False
        

