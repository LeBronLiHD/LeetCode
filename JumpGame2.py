# -*- coding: utf-8 -*-
# dp

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        dp = [[0] * size for _ in range(size)]


def main():
    obj = Solution()
    nums = [[2, 3, 1, 1, 4],
            [3, 2, 1, 0, 4],
            [1, 2, 3]]
    size = len(nums)
    for i in range(size):
        print(i, " -> ", obj.canJump(nums[i]))


if __name__ == "__main__":
    main()
