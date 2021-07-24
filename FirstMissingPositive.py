# -*- coding: utf-8 -*-
# Runtime: 604 ms
# Memory Usage: 67.5 MB

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        positive = [1]
        size = len(nums)
        for i in range(size):
            positive.append(i + 2)
        for i in range(size):
            temp = nums[i]
            if temp <= 0:
                continue
            if temp > size + 1:
                continue
            positive[temp - 1] = size + 2
        for i in range(size + 1):
            if positive[i] != size + 2:
                return positive[i]


def main():
    nums = [7, 8, 9, 11]
    obj = Solution()
    print("firstMissingPositive [7, 8, 9, 11]  = ", obj.firstMissingPositive(nums))
    nums = [1, 2, 0, -1]
    print("firstMissingPositive [1, 2, 0, -1]  = ", obj.firstMissingPositive(nums))
    nums = [1, 3, 4, -1]
    print("firstMissingPositive [1, 3, 4, -1]  = ", obj.firstMissingPositive(nums))
    nums = [1]
    print("firstMissingPositive [1]            = ", obj.firstMissingPositive(nums))
    nums = [1, 1, 1]
    print("firstMissingPositive [1, 1, 1]      = ", obj.firstMissingPositive(nums))
    nums = [1, 2, 6, 3, 5, 4]
    print("firstMissingPositive [1,2,6,3,5,4]  = ", obj.firstMissingPositive(nums))
    nums = [0, 2, 2, 1, 1]
    print("firstMissingPositive [0, 2, 2, 1, 1]= ", obj.firstMissingPositive(nums))


if __name__ == "__main__":
    main()
