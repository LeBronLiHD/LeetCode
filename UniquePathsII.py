# -*- coding: utf-8 -*-
# also, dp
# Runtime: 24 ms, faster than 92.11% of Python online submissions for Unique Paths II.
# Memory Usage: 13.5 MB, less than 62.39% of Python online submissions for Unique Paths II.

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows = len(obstacleGrid)
        if rows == 0:
            return 0
        cols = len(obstacleGrid[0])
        if obstacleGrid[rows - 1][cols - 1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        if obstacleGrid[rows - 2][cols - 1] != 1:
            obstacleGrid[rows - 2][cols - 1] = -1
        if obstacleGrid[rows - 1][cols - 2] != 1:
            obstacleGrid[rows - 1][cols - 2] = -1
        for i in range(rows - 3, -1, -1):
            if obstacleGrid[i][cols - 1] == 1:
                continue
            elif obstacleGrid[i + 1][cols - 1] != 1:
                obstacleGrid[i][cols - 1] = obstacleGrid[i + 1][cols - 1]
            else:
                obstacleGrid[i][cols - 1] = 1
        for i in range(cols - 3, -1, -1):
            if obstacleGrid[rows - 1][i] == 1:
                continue
            elif obstacleGrid[rows - 1][i + 1] != 1:
                obstacleGrid[rows - 1][i] = obstacleGrid[rows - 1][i + 1]
            else:
                obstacleGrid[rows - 1][i] = 1
        for i in range(cols - 2, -1, -1):
            for j in range(rows - 2, -1, -1):
                if obstacleGrid[j][i] == 1:
                    continue
                elif obstacleGrid[j][i + 1] == 1 and obstacleGrid[j + 1][i] == 1:
                    obstacleGrid[j][i] = 0
                elif obstacleGrid[j][i + 1] == 1:
                    obstacleGrid[j][i] = obstacleGrid[j + 1][i]
                elif obstacleGrid[j + 1][i] == 1:
                    obstacleGrid[j][i] = obstacleGrid[j][i + 1]
                else:
                    obstacleGrid[j][i] = obstacleGrid[j][i + 1] + obstacleGrid[j + 1][i]
        return -obstacleGrid[0][0]


def main():
    obj = Solution()
    maps = [[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]],
            [[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]],
            [[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 1]],
            [],
            [[1, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 1]],
            [[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]]
    size = len(maps)
    for i in range(size):
        print("unique paths of map[", i + 1, "]  -> ", obj.uniquePathsWithObstacles(maps[i]))


if __name__ == '__main__':
    main()
