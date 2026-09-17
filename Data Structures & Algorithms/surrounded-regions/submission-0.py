class Solution:
    def solve(self, board: List[List[str]]) -> None:
        prospective = set()
        queue  = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='O':
                    prospective.add(tuple([i,j]))
                    queue.append(tuple([i,j]))
                    while queue:
                        processing = queue.pop()
                        if processing[0] == 0 or processing[0] == len(board)-1 or processing[1]==0 or processing[1] == len(board[0]) - 1:
                            prospective.clear()
                            queue = []
                            break
                        for s,t in [(1,0),(-1,0),(0,1),(0,-1)]:
                            if board[processing[0]+s][processing[1]+t]=='O' and tuple([processing[0]+s,processing[1]+t]) not in prospective:
                                prospective.add(tuple([processing[0]+s,processing[1]+t]))
                                queue.append(tuple([processing[0]+s,processing[1]+t]))
                    if prospective:
                        for s,t in prospective:
                            board[s][t] = 'X'
                        