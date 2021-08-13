# -*- coding: utf-8 -*-
# Your goal is to reach the last index in the minimum number of jumps.
# dynamic programing
# Runtime: 170 ms, faster than 42.32% of Python online submissions for Jump Game II.
# Memory Usage: 14.3 MB, less than 70.26% of Python online submissions for Jump Game II.

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        maxJump, lastIndex, MinJumps = 0, 0, 0
        for i in range(size - 1):
            maxJump = max(maxJump, i + nums[i])
            # only when we have to jump one more time to jump to some specific index(position)
            # should we run: MinJumps += 1
            if i == lastIndex:
                # index = size - 1 means we already jump to the final index
                lastIndex = maxJump
                MinJumps += 1
        return MinJumps


def main():
    nums = [[2, 3, 1, 1, 4],
            [1, 2, 3],
            [2, 0, 0],
            [3, 0, 8, 2, 0, 0, 1],
            [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]]
    length = len(nums)
    obj = Solution()
    for i in range(length):
        print("array[", i, "] \t-> ", obj.jump(nums[i]))


if __name__ == "__main__":
    main()
