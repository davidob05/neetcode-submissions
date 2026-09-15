class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        i=0
        j=0
        count=0
        
        while i<len(grid):
            if grid[i][j] == '0':
                if j==len(grid[0])-1:
                    j = 0
                    i+=1
                else:
                    j+=1
                continue
            count+=1
            grid = self.rem_isl(grid,i,j)
            if j==len(grid[0])-1:
                j = 0
                i+=1
            else:
                j+=1
        
        return count

    def rem_isl(self, grid: List[List[str]], i: int, j: int) -> List[List[int]]:
        if i == len(grid) or j == len(grid[0]):
            return grid
        elif i<0 or j<0:
            return grid
        elif grid[i][j] == '0':
            return grid
        grid[i][j] = '0'
        self.rem_isl(grid,i,j-1)
        self.rem_isl(grid,i,j+1)
        self.rem_isl(grid,i+1,j)
        self.rem_isl(grid,i-1,j)
        return grid
        

