from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> None:
        queue = deque([])
        to_be_rotted = set()
        fresh = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append(tuple([i,j]))
                elif grid[i][j]==1:
                    fresh+=1

        time = 0
        

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

            if not to_be_rotted:
                break
            
            while len(to_be_rotted)>0:
                orange = to_be_rotted.pop()
                grid[orange[0]][orange[1]] = 2
                fresh-=1
                queue.append(tuple([orange[0],orange[1]]))
            
            time+=1

        
        return time if fresh ==0 else -1
                
                

                    


        