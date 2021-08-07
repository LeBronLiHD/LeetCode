# -*- coding: utf-8 -*-
# 使得横、竖和两个对角线方向均不会同时出现两个皇后
# Runtime: 133 ms, faster than 14.23% of Python online submissions for N-Queens.
# Memory Usage: 13.9 MB, less than 35.07% of Python online submissions for N-Queens.

class Solution(object):
    def solveNQueens(self, N: int):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = []
        board = [['.'] * N for _ in range(N)]

        def place(row: int):
            if row >= N:
                ans.append(["".join(string) for string in board])
                return
            for i in range(N):
                if isValid(row, i):
                    board[row][i] = 'Q'
                    place(row + 1)
                    board[row][i] = '.'

        def isValid(row: int, col: int):
            for i in range(N):
                if board[row][i] == 'Q' and col != i:
                    return False
                if board[i][col] == 'Q' and row != i:
                    return False
            cur_row, cur_col = row - 1, col - 1
            while cur_col >= 0 and cur_row >= 0:
                if board[cur_row][cur_col] == 'Q':
                    return False
                cur_row, cur_col = cur_row - 1, cur_col - 1
            cur_row, cur_col = row + 1, col + 1
            while cur_col < N and cur_row < N:
                if board[cur_row][cur_col] == 'Q':
                    return False
                cur_row, cur_col = cur_row + 1, cur_col + 1
            cur_row, cur_col = row + 1, col - 1
            while cur_row < N and cur_col >= 0:
                if board[cur_row][cur_col] == 'Q':
                    return False
                cur_row, cur_col = cur_row + 1, cur_col - 1
            cur_row, cur_col = row - 1, col + 1
            while cur_row >= 0 and cur_col < N:
                if board[cur_row][cur_col] == 'Q':
                    return False
                cur_row, cur_col = cur_row - 1, cur_col + 1
            return True

        place(0)
        return ans


def main():
    obj = Solution()
    maximum = 10
    nums = [i for i in range(1, maximum)]
    print(nums)
    for i in range(1, maximum):
        ans = obj.solveNQueens(i)
        print(i, " -> ", ans)


if __name__ == "__main__":
    main()
