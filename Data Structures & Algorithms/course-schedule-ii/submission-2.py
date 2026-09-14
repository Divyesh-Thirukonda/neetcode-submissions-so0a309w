class Solution:
    from collections import defaultdict
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 5, [[2, 1], [3, 1], [4, 2], [4, 3]]

        # 0: 
        # 1: 
        # 2: 1
        # 3: 1
        # 4: 2,3

        out = []
        
        indegree = [0]*numCourses
        adj = [[] for i in range(numCourses)]

        for course, prereq in prerequisites:
            adj[course].append(prereq)
            indegree[prereq] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        doneSoFar = 0
        while q:
            node = q.popleft()
            out.append(node)
            doneSoFar += 1
            for course in adj[node]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)

        if numCourses != doneSoFar:
            return []

        return out[::-1]