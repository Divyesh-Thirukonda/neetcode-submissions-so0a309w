class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = []

        adj = [[] for _ in range(numCourses)]
        '''
        0: [2]
        1: [0]
        2: [1]
        '''
        inDegree = [0] * numCourses
        '''
        1,1,1
        '''

        for canTake, prereq in prerequisites:
            inDegree[canTake] += 1
            adj[prereq].append(canTake)


        def dfs(node):
            inDegree[node] -=1
            output.append(node)

            for nei in adj[node]:
                inDegree[nei] -=1
                if inDegree[nei] == 0:
                    dfs(nei)

        for c in range(numCourses):
            if inDegree[c] == 0:
                dfs(c)

        return output if len(output) == numCourses else []

            