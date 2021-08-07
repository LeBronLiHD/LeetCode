# -*- coding: utf-8 -*-

class Solution(object):
    def totalNQueens(self, N):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        board = [['.'] * N for _ in range(N)]

        def place(i: int, vert: int, ldiag: int, rdiag: int) -> None:
            if i == N:
                ret += 1
                return
            for j in range(N):
                vmask, lmask, rmask = 1 << j, 1 << (i + j), 1 << (N - i - 1 + j)
                if vert & vmask or ldiag & lmask or rdiag & rmask:
                    continue
                board[i][j] = 'Q'
                place(i + 1, vert | vmask, ldiag | lmask, rdiag | rmask)
                board[i][j] = '.'

        place(0, 0, 0, 0)
        return ret


def main():
    obj = Solution()
    maximum = 10
    nums = [i for i in range(1, maximum)]
    print(nums)
    for i in range(1, maximum):
        ans = obj.totalNQueens(i)
        print(i, " -> ", ans)

if __name__ == "__main__":
    main()
