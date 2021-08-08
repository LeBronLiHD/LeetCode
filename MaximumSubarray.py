# -*- coding: utf-8 -*-
# 200 / 203
# Time Limit Exceeded

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        # matrix = [[0] * size for _ in range(size)]
        max_val = -100000
        for i in range(size):
            for j in range(i, size):
                sum_val = 0
                for index in range(i, j + 1):
                    sum_val += nums[index]
                if sum_val > max_val:
                    max_val = sum_val
        return max_val


def main():
    obj = Solution()
    nums = [[-2, 1, -3, 4, -1, 2, 1, -5, 4],
            [5, 4, -1, 7, 8],
            [9]]
    size = len(nums)
    for i in range(size):
        print(i, " -> ", obj.maxSubArray(nums[i]))


if __name__ == "__main__":
    main()
