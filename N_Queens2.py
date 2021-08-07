# -*- coding: utf-8 -*-
# 使得横、竖和两个对角线方向均不会同时出现两个皇后

class Solution(object):
    def solveNQueens(self, N: int):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = []
        board = [['.'] * N for _ in range(N)]

        def place(i: int, vert: int, ldiag: int, rdiag: int) -> None:
            if i == N:
                ans.append(["".join(row) for row in board])
                return
            for j in range(N):
                vmask, lmask, rmask = 1 << j, 1 << (i + j), 1 << (N - i - 1 + j)
                if vert & vmask or ldiag & lmask or rdiag & rmask:
                    continue
                board[i][j] = 'Q'
                place(i + 1, vert | vmask, ldiag | lmask, rdiag | rmask)
                board[i][j] = '.'

        place(0, 0, 0, 0)
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
