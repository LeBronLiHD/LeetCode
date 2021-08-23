# -*- coding: utf-8 -*-
# Runtime: 8 ms, faster than 99.72% of Python online submissions for Spiral Matrix II.
# Memory Usage: 13.3 MB, less than 72.44% of Python online submissions for Spiral Matrix II.

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        depth = 0
        index = 1
        ansMatrix = [[0] * n for _ in range(n)]
        while index <= n * n:
            for i in range(depth, n - depth):
                ansMatrix[depth][i] = index
                index += 1
            for i in range(depth + 1, n - depth):
                ansMatrix[i][n - depth - 1] = index
                index += 1
            for i in range(n - depth - 2, depth - 1, -1):
                ansMatrix[n - depth - 1][i] = index
                index += 1
            for i in range(n - depth - 2, depth, -1):
                ansMatrix[i][depth] = index
                index += 1
            depth += 1
        # for i in range(n):
        #     print(ansMatrix[i])
        return ansMatrix


def main():
    nums = [3, 5, 6, 7, 8, 20]
    length = len(nums)
    obj = Solution()
    for i in range(length):
        print(nums[i], " -> ", obj.generateMatrix(nums[i]))


if __name__ == "__main__":
    main()
