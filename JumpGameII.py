# -*- coding: utf-8 -*-
# Your goal is to reach the last index in the minimum number of jumps.
# recursion
# Runtime: 8672 ms, faster than 9.14% of Python3 online submissions for Jump Game II.
# Memory Usage: 30.7 MB, less than 5.02% of Python3 online submissions for Jump Game II.

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memory = {}
        size = len(nums)

        def find_min_jumps(start_index):
            if start_index in memory:
                return memory[start_index]
            if start_index == size - 1:
                memory[start_index] = 0
                return 0
            jumps = nums[start_index]
            if size - 1 - start_index <= jumps:
                memory[start_index] = 1
                return 1
            if jumps == 0:
                return size + 1
            jump_list = []
            for i in range(jumps):
                jump_list.append(1 + find_min_jumps(start_index + i + 1))
            memory[start_index] = min(jump_list)
            return memory[start_index]

        return find_min_jumps(0)


def main():
    nums = [[2, 3, 1, 1, 4],
            [2, 3, 0, 1, 4]]
    length = len(nums)
    obj = Solution()
    for i in range(length):
        print("array[", i, "] \t-> ", obj.jump(nums[i]))


if __name__ == "__main__":
    main()
