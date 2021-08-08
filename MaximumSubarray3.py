# -*- coding: utf-8 -*-
# Dynamic Programming
# Runtime: 36 ms, faster than 99.44% of Python online submissions for Maximum Subarray.
# Memory Usage: 13.9 MB, less than 95.61% of Python online submissions for Maximum Subarray.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        cur_sum = 0
        for i in range(0, len(nums)):
            cur_sum += nums[i]
            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return max_sum


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
