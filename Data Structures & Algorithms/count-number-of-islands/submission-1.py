class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.rem_isl(grid, i, j)
            
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
        

