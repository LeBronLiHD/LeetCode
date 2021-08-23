# -*- coding: utf-8 -*-
# also also, dynamic programming
# Runtime: 64 ms, faster than 99.51% of Python online submissions for Minimum Path Sum.
# Memory Usage: 14.4 MB, less than 90.70% of Python online submissions for Minimum Path Sum.

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows - 2, -1, -1):
            grid[i][cols - 1] += grid[i + 1][cols - 1]
        for i in range(cols - 2, -1, -1):
            grid[rows - 1][i] += grid[rows - 1][i + 1]
        for j in range(cols - 2, -1, -1):
            for i in range(rows - 2, -1, -1):
                grid[i][j] += min(grid[i + 1][j], grid[i][j + 1])
        return grid[0][0]


def main():
    obj = Solution()
    grids = [[[1, 3, 1], [1, 5, 1], [4, 2, 1]],
             [[1, 2, 3], [4, 5, 6]]]
    size = len(grids)
    for i in range(size):
        print("gird[", i + 1, "] -> ", obj.minPathSum(grids[i]))


if __name__ == '__main__':
    main()
