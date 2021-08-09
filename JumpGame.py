# -*- coding: utf-8 -*-
# recursion
# 75 / 166
# Time Limit Exceeded

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        memory = {}
        size = len(nums)
        def jumpOrNot(initIndex):
            if initIndex in memory:
                return memory[initIndex]
            if initIndex == size - 1:
                memory[initIndex] = True
                return True
            jumpRange = nums[initIndex]
            if size - 1 <= initIndex + jumpRange:
                memory[initIndex] = True
                return True
            if jumpRange == 0:
                memory[initIndex] = False
                return False
            for i in range(1, jumpRange + 1):
                if jumpOrNot(i + initIndex):
                    memory[initIndex] = True
                    return True
            memory[initIndex] = False
            return False
        return jumpOrNot(0)


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
