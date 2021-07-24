# -*- coding: utf-8 -*-

class Solution(object):
    def find_in_row(self, board, row, num):
        for i in range(9):
            if ord(board[row][i]) == ord('0') + num:
                return False
        return True

    def find_in_col(self, board, col, num):
        for i in range(9):
            if ord(board[i][col]) == ord('0') + num:
                return False
        return True

    def find_in_cubic(self, board, row, col, num):
        for row_index in range(3):
            for col_index in range(3):
                if ord(board[int(row/3)*3 + row_index][int(col/3)*3 + col_index]) == ord('0') + num:
                    return False
        return True

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        every_unit = []  # [row, col, number[]]
        loop_count = 0
        while len(every_unit) > 0 or loop_count == 0:
            every_unit = []
            loop_count += 1
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        available = []
                        for num in range(9):
                            num += 1
                            if self.find_in_row(board, row, num) and \
                                    self.find_in_col(board, col, num) and \
                                    self.find_in_cubic(board, row, col, num):
                                available.append(num)
                        if len(available) == 1:
                            board[row][col] = ascii(available[0])
                        every_unit.append([row, col, available])
                    else:
                        continue


def main():
    obj = Solution()
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    obj.solveSudoku(board)
    for i in range(9):
        print(board[i])

if __name__ == "__main__":
    main()
