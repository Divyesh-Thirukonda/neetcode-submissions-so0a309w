class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        numFresh = 0
        timer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    numFresh += 1

        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]

        while numFresh > 0 and queue:
            length = len(queue)

            for i in range(length):
                node = queue.popleft()

                for dire in directions:
                    newDir = (dire[0] + node[0], dire[1] + node[1])
                    if not (0 <= newDir[0] < len(grid)) or not (0 <= newDir[1] < len(grid[0])):
                        continue
                    
                    if grid[newDir[0]][newDir[1]] == 1:
                        grid[newDir[0]][newDir[1]] = 2
                        queue.append((newDir[0], newDir[1]))
                        numFresh -= 1
        
            timer += 1 # to test

        if numFresh > 0:
            return -1
        return timer