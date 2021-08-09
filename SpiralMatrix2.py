# -*- coding: utf-8 -*-
# Runtime: 16 ms, faster than 75.97% of Python online submissions for Spiral Matrix.
# Memory Usage: 13.3 MB, less than 71.23% of Python online submissions for Spiral Matrix.

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        depth = 0
        rows = len(matrix)
        cols = len(matrix[0])
        while True:
            for i in range(depth, cols - depth):
                ans.append(matrix[depth][i])
            for i in range(1 + depth, rows - depth):
                ans.append(matrix[i][cols - 1 - depth])
            if len(ans) >= cols * rows:
                break
            for i in range(cols - 2 - depth, -1 + depth, -1):
                ans.append(matrix[rows - 1 - depth][i])
            for i in range(rows - depth - 2, depth, -1):
                ans.append(matrix[i][depth])
            if len(ans) >= cols * rows:
                break
            depth += 1
        return ans


def main():
    obj = Solution()
    matrixs = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
               [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
               [[7], [9], [6]],
               [[7, 7], [9, 9], [6, 6]],
               [[2, 5, 8], [4, 0, -1]]]
    size = len(matrixs)
    for i in range(size):
        print(i + 1, " -> ", obj.spiralOrder(matrixs[i]))


if __name__ == "__main__":
    main()
