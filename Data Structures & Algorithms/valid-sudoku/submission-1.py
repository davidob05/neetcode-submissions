class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            if not self.checkDuplicates(board[i]) or not self.checkDuplicates([board[j][i] for j in range(len(board))]):
                return False
            elif i%3==0:
                for j in range(0,len(board),3):
                    if not self.checkDuplicates([board[r][c] for r in range(i, i+3) for c in range(j, j+3)]):
                        return False
        return True

    def checkDuplicates(self, subset: List[str]) -> bool:
        nums = set()
        for char in subset:
            if char != ".":
                if char in nums:
                    return False
                nums.add(char)
        return True