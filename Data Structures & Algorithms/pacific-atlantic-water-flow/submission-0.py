class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = {}
        atl = {}
        
        for i in range(len(heights[0])):
            pac[tuple([0, i])] = heights[0][i]
            atl[tuple([len(heights)-1, i])] = heights[len(heights)-1][i]
        for i in range(len(heights)):
            pac[tuple([i,0])] = heights[i][0]
            atl[tuple([i, len(heights[0])-1])] = heights[i][len(heights[0])-1]
        queue = list(pac.keys())
        while queue:
            r, c = queue.pop()
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < len(heights) and 0 <= nc < len(heights[0]):
                    if (nr, nc) not in pac and heights[nr][nc] >= heights[r][c]:
                        pac[(nr, nc)] = heights[nr][nc]
                        queue.append((nr, nc))
        
        queue = list(atl.keys())
        while queue:
            r, c = queue.pop()
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < len(heights) and 0 <= nc < len(heights[0]):
                    if (nr, nc) not in atl and heights[nr][nc] >= heights[r][c]:
                        atl[(nr, nc)] = heights[nr][nc]
                        queue.append((nr, nc))
        
        result = []
        for key in pac.keys():
            if key in atl:
                result.append(key)
        return result
        

        
                

                
                
                


                


                