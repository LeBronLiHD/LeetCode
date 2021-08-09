# -*- coding: utf-8 -*-
# memory
# # 74 / 166
# Time Limit Exceeded

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        dp = [[0] * (size + 1) for _ in range(size + 1)]
        dp[0][1] = 1

        for i in range(size):
            jumpCover = nums[i]
            initJump = -1
            # store the past jumps
            for j in range(i + 1, size + 1):
                if dp[i][j] == 1:
                    dp[i + 1][j] = 1
            # judge the condition of current jump
            if dp[i][i + 1] == 1:
                dp[i + 1][i + 1] = 1
                initJump = i + 1
            # if no current jump happen
            if initJump == -1:
                continue
            # if current jump happen
            for j in range(jumpCover):
                if j + initJump + 1 <= size:
                    dp[i + 1][j + initJump + 1] = 1

        return dp[size][size] == 1


def main():
    obj = Solution()
    nums = [[2, 3, 1, 1, 4],
            [3, 2, 1, 0, 4],
            [1, 2, 3],
            [2, 0, 0],
            [3, 0, 8, 2, 0, 0, 1],
            [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]]
    size = len(nums)
    for i in range(size):
        print(i, " -> ", obj.canJump(nums[i]))


if __name__ == "__main__":
    main()
