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
        valid_set = False
        while len(every_unit) > 0 or loop_count == 0:
            every_unit = []
            loop_count += 1
            valid_set = False
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
                            # print([row, col, available])
                            board[row][col] = chr(ord('0') + available[0])
                            valid_set = True
                        else:
                            every_unit.append([row, col, available])
                    else:
                        continue
            # for i in range(9):
            #     print(board[i])
            if valid_set == True:
                continue
            else:
                size = len(every_unit)
                if size == 0:
                    print("done!")
                    return
                min_size = 9
                min_index = 0
                for iii in range(size):
                    if len(every_unit[iii][2]) < min_size:
                        min_size = len(every_unit[iii][2])
                        min_index = iii
                if min_size == 0:
                    return
                else:
                    for i in range(min_size):
                        if i != min_size - 1:
                            copy_board = []
                            for row in range(9):
                                row_list = []
                                for col in range(9):
                                    row_list.append(board[row][col])
                                copy_board.append(row_list)
                            board[every_unit[min_index][0]][every_unit[min_index][1]] = chr(ord('0') + every_unit[min_index][2][i])
                            # if self.find_in_row(board, every_unit[min_index][0], every_unit[min_index][2][i])\
                            #     and self.find_in_col(board, every_unit[min_index][1], every_unit[min_index][2][i])\
                            #     and self.find_in_cubic(board, every_unit[min_index][0], every_unit[min_index][1], every_unit[min_index][2][i]):
                            #     board[every_unit[min_index][0]][every_unit[min_index][1]] = chr(ord('0') + every_unit[min_index][2][i])
                            # else:
                            #     print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
                            self.solveSudoku(board)
                            flag = True
                            for row in range(9):
                                for col in range(9):
                                    if board[row][col] == '.':
                                        flag = False
                            if ~flag:
                                for row in range(9):
                                    for col in range(9):
                                        board[row][col] = copy_board[row][col]
                                del copy_board
                            else:
                                return
                        else:
                            board[every_unit[min_index][0]][every_unit[min_index][1]] = chr(ord('0') + every_unit[min_index][2][i])
                            self.solveSudoku(board)
                            return
        return


def main():
    print("ERROR VERSION!")
    obj = Solution()
    board = [[".", ".", ".", "2", ".", ".", ".", "6", "3"],
             ["3", ".", ".", ".", ".", "5", "4", ".", "1"],
             [".", ".", "1", ".", ".", "3", "9", "8", "."],
             [".", ".", ".", ".", ".", ".", ".", "9", "."],
             [".", ".", ".", "5", "3", "8", ".", ".", "."],
             [".", "3", ".", ".", ".", ".", ".", ".", "."],
             [".", "2", "6", "3", ".", ".", "5", ".", "."],
             ["5", ".", "3", "7", ".", ".", ".", ".", "8"],
             ["4", "7", ".", ".", ".", "1", ".", ".", "."]]
    obj.solveSudoku(board)
    for i in range(9):
        print(board[i])
    print("===============================================================")
    board_2 = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    obj.solveSudoku(board_2)
    for i in range(9):
        print(board_2[i])


if __name__ == "__main__":
    main()
