# -*- coding: utf-8 -*-
# Runtime: 36 ms, faster than 65.45% of Python3 online submissions for Rotate Image.
# Memory Usage: 14.4 MB, less than 5.25% of Python3 online submissions for Rotate Image.

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)  # width = length
        mid = int(n/2)
        add = 0
        if n % 2 == 1:
            add += 1
        # matrix[i][j]
        # -> matrix[j][n - i - 1]
        # -> matrix[n - i - 1][n - j - 1]
        # -> matrix[n - j - 1][n - (n - i - 1) - 1] -> matrix[n - j - 1][i]
        # -> matrix[i][j]
        for i in range(mid):
            for j in range(mid + add):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = temp
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
