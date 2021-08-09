# -*- coding: utf-8 -*-
# dynamic programming
# Runtime: 416 ms, faster than 57.85% of Python online submissions for Jump Game.
# Memory Usage: 14.6 MB, less than 46.78% of Python online submissions for Jump Game.

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        maxJump = 0
        for i in range(size):
            if maxJump < i:
                return False
            curJump = i + nums[i]
            maxJump = max(maxJump, curJump)
            if maxJump >= size - 1:
                return True
        return False


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
