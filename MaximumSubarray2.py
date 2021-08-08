# -*- coding: utf-8 -*-
# 201 / 203
# Time Limit Exceeded

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        # matrix = [[0] * size for _ in range(size)]
        matrix = {}
        max_val = float("-inf")
        matrix[(0, 0)] = nums[0]  # init
        for i in range(size):
            for j in range(i, size):
                if (i, j) in matrix:
                    # print("impossible!")
                    if matrix[(i, j)] > max_val:
                        max_val = matrix[(i, j)]
                    continue
                elif j >= 1 and (i, j - 1) in matrix:
                    matrix[(i, j)] = matrix[(i, j - 1)] + nums[j]
                elif i >= 1 and (i - 1, j) in matrix:
                    matrix[(i, j)] = matrix[(i - 1, j)] - nums[i - 1]
                else:
                    print("impossible!")
                    temp_sum = 0
                    for index in range(i, j + 1):
                        temp_sum += nums[index]
                    matrix[(i, j)] = temp_sum
                if matrix[(i, j)] > max_val:
                    max_val = matrix[(i, j)]
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
