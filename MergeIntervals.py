# -*- coding: utf-8 -*-

# Runtime: 132 ms, faster than 5.16% of Python online submissions for Merge Intervals.
# Memory Usage: 15.7 MB, less than 82.82% of Python online submissions for Merge Intervals.

# Runtime: 68 ms, faster than 58.14% of Python online submissions for Merge Intervals.
# Memory Usage: 15.8 MB, less than 56.31% of Python online submissions for Merge Intervals.

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        size = len(intervals)
        i = 0
        while i < size:
            j = 1
            while i + j < size and intervals[i + j][0] <= intervals[i + j - 1][1]:
                intervals[i][1] = max(intervals[i][1], intervals[i + j][1])
                j += 1
            if j == 1:
                i += 1
                continue
            else:
                for k in range(j - 1):
                    intervals.remove(intervals[i + 1])
                    size -= 1
        return intervals


def main():
    nums = [[[1, 3], [2, 6], [8, 10], [15, 18]],
            [[1, 4], [4, 5]],
            [[1, 3], [2, 6], [6, 10], [10, 18]],
            [[1, 4], [0, 4]],
            [[1, 4], [0, 1]],
            [[1, 4], [0, 5]],
            [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]]
    length = len(nums)
    obj = Solution()
    for i in range(length):
        print("nums[", i + 1, "]", " -> ", obj.merge(nums[i]))


if __name__ == "__main__":
    main()
