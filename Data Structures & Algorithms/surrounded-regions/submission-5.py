class Solution:
    def solve(self, board: List[List[str]]) -> None:
        prospective = set()
        queue  = []
        visited = [[False]*len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='O' and not visited[i][j]:
                    touches_border = False
                    prospective.add(tuple([i,j]))
                    visited[i][j] = True
                    queue.append(tuple([i,j]))
                    while queue:
                        processing = queue.pop()
                        if processing[0] == 0 or processing[0] == len(board)-1 or processing[1]==0 or processing[1] == len(board[0]) - 1:
                            touches_border = True
                        for s,t in [(1,0),(-1,0),(0,1),(0,-1)]:
                            newi, newj = processing[0]+s, processing[1]+t
                            if 0 <= newi < len(board) and 0 <= newj < len(board[0]) and board[newi][newj]=='O' and not visited[newi][newj]:
                                visited[newi][newj] = True
                                prospective.add(tuple([newi,newj]))
                                queue.append(tuple([newi,newj]))
                    if not touches_border:
                        for s,t in prospective:
                            board[s][t] = 'X'
                    prospective = set()