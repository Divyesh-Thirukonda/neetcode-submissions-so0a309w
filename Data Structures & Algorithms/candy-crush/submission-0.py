class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        # do BFS to find all candies on left (if left, keep going left... same for right)
        # if len of returned bfs >= 3, set all in queue to 0

        # handle gravity
        # bubble the 0 upwards for each col

        # end when bfs returns len 0

        width = len(board[0])
        height = len(board)
        def find():
            seen = set()
                
            for i in range(1, height-1):
                for j in range(width):
                    if board[i][j] == 0:
                        continue
                    if board[i+1][j] == board[i-1][j] == board[i][j]:
                        seen.add((i+1, j))
                        seen.add((i-1, j))
                        seen.add((i, j))

            for i in range(height):
                for j in range(1, width-1):
                    if board[i][j] == 0:
                        continue
                    if board[i][j+1] == board[i][j-1] == board[i][j]:
                        seen.add((i, j+1))
                        seen.add((i, j-1))
                        seen.add((i, j))
            return seen

        def crush(seen):
            for i, j in seen:
                board[i][j] = 0

        def drop():
            for col in range(width):
                lowest0 = -1

                for row in range(height - 1, -1, -1):
                    if board[row][col] == 0:
                        lowest0 = max(lowest0, row)
                    elif lowest0 >= 0:
                        board[row][col], board[lowest0][col] = board[lowest0][col], board[row][col]
                        lowest0 -= 1

        
        seen = find()
        while seen:
            crush(seen)
            drop()
            seen = find()
        return board