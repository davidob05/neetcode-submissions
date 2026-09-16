from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> None:
        queue = deque([])
        to_be_rotted = set()
        fresh = 0
        rotten_count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append(tuple([i,j]))
                elif grid[i][j]==1:
                    fresh+=1
                    
        time = 0
        if len(queue)==0 and fresh == 0:
            return 0
        elif len(queue) == 0 and fresh > 0:
            return -1

        while len(queue)>0:
            while len(queue)>0:
                elt = queue.popleft()
                i,j = elt[0],elt[1]
                if i>0 and grid[i-1][j] == 1:
                    to_be_rotted.add(tuple([i-1,j]))
                    
                if i<len(grid) - 1 and grid[i+1][j] == 1:
                    to_be_rotted.add(tuple([i+1,j]))

                if j>0 and grid[i][j-1] == 1:
                    to_be_rotted.add(tuple([i,j-1]))

                if j< len(grid[0]) - 1 and grid[i][j+1] == 1:
                    to_be_rotted.add(tuple([i,j+1]))

            
            
            while len(to_be_rotted)>0:
                orange = to_be_rotted.pop()
                grid[orange[0]][orange[1]] = 2
                fresh-=1
                queue.append(tuple([orange[0],orange[1]]))
            
            time+=1

        
        return time - 1 if fresh ==0 else -1
                
                

                    


        