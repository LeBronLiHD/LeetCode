# -*- coding: utf-8 -*-
# Runtime: 52 ms, faster than 49.28% of Python online submissions for N-Queens II.
# Memory Usage: 13.8 MB, less than 9.71% of Python online submissions for N-Queens II.

class Solution(object):
    def totalNQueens(self, N):
        """
        :type n: int
        :rtype: int
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
        return len(ans)


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
