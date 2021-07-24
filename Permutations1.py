# -*- coding: utf-8 -*-
# Runtime: 40 ms, faster than 70.92% of Python3 online submissions for Permutations.
# Memory Usage: 14.3 MB, less than 89.04% of Python3 online submissions for Permutations.

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        ret = []
        if length == 1:
            ret.append(nums)
            return ret
        for i in range(length):
            lists = self.permute(nums[0:i] + nums[i + 1:length])
            temp_length = len(lists)
            for j in range(temp_length):
                lists[j].append(nums[i])
                ret.append(lists[j])
        return ret


def main():
    obj = Solution()
    nums = [
        [1, 2, 3]
    ]
    size = len(nums)
    for i in range(size):
        lists = obj.permute(nums[i])
        print(lists)


if __name__ == "__main__":
    main()
