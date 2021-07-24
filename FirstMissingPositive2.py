# -*- coding: utf-8 -*-
# Runtime: 512 ms, faster than 80.47% of Python online submissions for First Missing Positive.
# Memory Usage: 48.2 MB, less than 42.93% of Python online submissions for First Missing Positive.

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        last_temp = 0
        ans = 1
        nums.sort()
        for i in range(size):
            temp = nums[i]
            if temp <= 0:
                continue
            elif ans == temp:
                ans = temp + 1
                last_temp = temp
            elif temp != last_temp:
                return ans
            else:
                last_temp = temp
        return ans


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
