# -*- coding: utf-8 -*-
# Divide and Conquer
# Runtime: 116 ms, faster than 5.15% of Python online submissions for Maximum Subarray.
# Memory Usage: 14.2 MB, less than 50.79% of Python online submissions for Maximum Subarray.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def divideAndConquer(left_index, right_index):
            if left_index == right_index:
                return nums[left_index]
            mid_index = (left_index + right_index) // 2  # divide result in integer
            left_max = divideAndConquer(left_index, mid_index)
            right_max = divideAndConquer(mid_index + 1, right_index)
            temp_sum, left, right = 0, float("-inf"), float("-inf")
            for i in range(mid_index, left_index - 1, -1):
                temp_sum += nums[i]
                left = max(left, temp_sum)
            temp_sum = 0
            for i in range(mid_index + 1, right_index + 1):
                temp_sum += nums[i]
                right = max(right, temp_sum)
            return max(left_max, right_max, left + right)

        return divideAndConquer(0, len(nums) - 1)


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
