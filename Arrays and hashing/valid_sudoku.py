class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        temp_arr = [["" for _ in range(9)] for _ in range(9)]
        second_arr = [[] for _ in range(9)]
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                temp_arr[i][j] = board[j][i]

        for i in range(len(board)):
            for j in range(len(board)):
                second_arr[i // 3 * 3 + j // 3].append(board[i][j])
        
        for i in board:
            if self.checkDuplicates(i):
                return False

        for i in temp_arr:
            if self.checkDuplicates(i):
                return False
        
        for i in second_arr:
            if self.checkDuplicates(i):
                return False

        return True
            
    def checkDuplicates(self, arr):
        count = 0
        for i in arr:
            if i == ".":
                count += 1
        if len(set(arr)) + count == 10:
            return False
        return True
        
        

        

solution = Solution()
print(solution.isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))