class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols = len(board),len(board[0])
        queue = []

        for i in range(cols):
            if board[0][i]=='O':
                queue.append((0,i))
                board[0][i] = 'Y'
            if board[rows-1][i]=='O':
                board[rows-1][i] = 'Y'
                queue.append((rows-1,i))
        for i in range(1,rows-1):
            if board[i][0] =='O':
                queue.append((i,0))
                board[i][0] = 'Y'
            if board[i][cols-1]=='O':
                queue.append((i,cols-1))
                board[i][cols-1] = 'Y'
        
        while queue:
            h,k = queue.pop()
            for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                if 0<=h+i <rows and 0<=j+k<cols and board[h+i][j+k]=='O':
                    queue.append((h+i,j+k))
                    board[h+i][j+k] = 'Y'
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Y':
                    board[i][j] = 'O'
        
        