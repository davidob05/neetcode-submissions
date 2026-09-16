class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        sizes = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid,size = rem_isl(grid, i, j)
                    sizes.add(size)
        if len(sizes)==0:
            return 0
        return max(sizes)
            



def rem_isl(grid: List[List[str]], i: int, j: int, size=0) -> List[List[int]]:

    if i == len(grid) or j == len(grid[0]):
        return grid, size
    elif i<0 or j<0:
        return grid, size
    elif grid[i][j] == 0:
        return grid, size
    grid[i][j] = 0

    if i > 0 and grid[i-1][j] == 1:
        grid,intermed_size = rem_isl(grid, i-1, j)
        size+=intermed_size
    if i < len(grid)-1 and grid[i+1][j] == 1:
        grid,intermed_size = rem_isl(grid, i+1, j)
        size+=intermed_size
    if j > 0 and grid[i][j-1] == 1:
        grid,intermed_size = rem_isl(grid, i, j-1)
        size+=intermed_size

    if j < len(grid[0])-1 and grid[i][j+1] == 1:
        grid,intermed_size = rem_isl(grid, i, j+1)
        size+=intermed_size
    size+=1
    return grid,size
                
                