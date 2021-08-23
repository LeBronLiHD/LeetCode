# -*- coding: utf-8 -*-
# Dynamic Programming
# Runtime: 16 ms, faster than 80.84% of Python online submissions for Unique Paths.
# Memory Usage: 13.5 MB, less than 21.80% of Python online submissions for Unique Paths.
# Runtime: 20 ms, faster than 53.99% of Python online submissions for Unique Paths.
# Memory Usage: 13.2 MB, less than 91.97% of Python online submissions for Unique Paths.

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 2] = 1
        dp[m - 2][n - 1] = 1
        for i in range(m - 3, -1, -1):
            dp[i][n - 1] = dp[i + 1][n - 1]
        for i in range(n - 3, -1, -1):
            dp[m - 1][i] = dp[m - 1][i + 1]
        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                dp[j][i] = dp[j + 1][i] + dp[j][i + 1]
        return dp[0][0]


def main():
    obj = Solution()
    nums_m = [6, 3, 3]
    nums_n = [3, 6, 7]
    size = len(nums_n)
    for i in range(size):
        print("uniquePath(", nums_m[i], nums_n[i], ") = ", obj.uniquePaths(nums_m[i], nums_n[i]))


if __name__ == '__main__':
    main()

'''

0 0 0 0 3 1 0
0 0 0 0 2 1 0
0 0 0 0 1 0 0
0 0 0 0 0 0 0
'''
