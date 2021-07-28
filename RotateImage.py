# -*- coding: utf-8 -*-
# Runtime: 16 ms, faster than 95.29% of Python online submissions for Rotate Image.
# Memory Usage: 13.2 MB, less than 92.33% of Python online submissions for Rotate Image.

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)  # width = length
        matrix.reverse()
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)


def main():
    obj = Solution()
    nums = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
        [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
        [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
        [[99999]]
    ]
    size = len(nums)
    for i in range(size):
        obj.rotate(nums[i])


if __name__ == "__main__":
    main()
