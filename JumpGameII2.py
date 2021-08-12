# -*- coding: utf-8 -*-
# Your goal is to reach the last index in the minimum number of jumps.
# Runtime: 9624 ms, faster than 6.75% of Python online submissions for Jump Game II.
# Memory Usage: 14.5 MB, less than 37.46% of Python online submissions for Jump Game II.

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        memory = [-1 for _ in range(size)]
        memory[0] = 0
        for i in range(size):
            if memory[i] == -1:
                continue
            else:
                for j in range(nums[i]):
                    if i + j + 1 < size:
                        if memory[i + j + 1] == -1:
                            memory[i + j + 1] = memory[i] + 1
                        else:
                            memory[i + j + 1] = min(memory[i + j + 1], memory[i] + 1)
        return memory[size - 1]


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
