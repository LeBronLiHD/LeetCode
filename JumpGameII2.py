# -*- coding: utf-8 -*-
# Your goal is to reach the last index in the minimum number of jumps.
# dynamic programing

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size <= 1:
            return 0
        dp = [[0] * size for _ in range(size)]
        jump_first = nums[0]
        for i in range(jump_first):
            dp[i][0] = 1
        for i in range(size - 1):
            i += 1
            jump_length = nums[i]



def main():
    nums = [[2, 3, 1, 1, 4]]
    length = len(nums)
    obj = Solution()
    for i in range(length):
        print("array[", i, "] \t-> ", obj.jump(nums[i]))


if __name__ == "__main__":
    main()

"""
[2, 3, 1, 1, 4] ->

1  0  0  0  0
1  1  1  1  0
1  0  0  0  0
0  0  0  0  0
0  0  0  0  0

"""
