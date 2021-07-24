# -*- coding: utf-8 -*-
# Runtime: 52 ms, faster than 57.49% of Python online submissions for Permutations II.
# Memory Usage: 13.6 MB, less than 85.03% of Python online submissions for Permutations II.

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        ret = []
        no_repeat = {}
        if length == 1:
            ret.append(nums)
            return ret
        for i in range(length):
            if nums[i] not in no_repeat:
                no_repeat[nums[i]] = i
                lists = self.permuteUnique(nums[0:i] + nums[i + 1:length])
                temp_length = len(lists)
                for j in range(temp_length):
                    lists[j].append(nums[i])
                    ret.append(lists[j])
        return ret


def main():
    obj = Solution()
    nums = [
        [1, 2, 3],
        [1, 1, 2]
    ]
    size = len(nums)
    for i in range(size):
        lists = obj.permuteUnique(nums[i])
        print(lists)


if __name__ == "__main__":
    main()
