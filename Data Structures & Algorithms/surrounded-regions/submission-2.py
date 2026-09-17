class Solution:
    def solve(self, board: List[List[str]]) -> None:
        prospective = set()
        queue  = []
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='O' and (i,j) not in visited:
                    touches_border = False
                    prospective.add(tuple([i,j]))
                    visited.add(tuple([i,j]))
                    queue.append(tuple([i,j]))
                    while queue:
                        processing = queue.pop()
                        if processing[0] == 0 or processing[0] == len(board)-1 or processing[1]==0 or processing[1] == len(board[0]) - 1:
                            touches_border = True
                        for s,t in [(1,0),(-1,0),(0,1),(0,-1)]:
                            if 0 <= processing[0]+s < len(board) and 0 <= processing[1]+t < len(board[0]) and board[processing[0]+s][processing[1]+t]=='O' and tuple([processing[0]+s,processing[1]+t]) not in visited:
                                visited.add(tuple([processing[0]+s,processing[1]+t]))
                                prospective.add(tuple([processing[0]+s,processing[1]+t]))
                                queue.append(tuple([processing[0]+s,processing[1]+t]))
                    if not touches_border:
                        for s,t in prospective:
                            board[s][t] = 'X'
                    prospective = set()