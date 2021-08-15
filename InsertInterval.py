# -*- coding: utf-8 -*-
# Runtime: 68 ms, faster than 27.48% of Python online submissions for Insert Interval.
# Memory Usage: 16.7 MB, less than 79.57% of Python online submissions for Insert Interval.

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        size = len(intervals)
        for i in range(size):
            if intervals[i][0] >= newInterval[0]:
                intervals.insert(i, newInterval)
                break
            elif i == size - 1:
                intervals.insert(size, newInterval)
                break
            else:
                continue
        if size == 0:
            intervals.append(newInterval)
        i = 0
        size += 1
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
    nums = [[[1, 3], [6, 9]],
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [],
            [[1, 5]],
            [[1, 5]]]
    newNums = [[2, 5],
               [4, 8],
               [5, 7],
               [2, 3],
               [2, 7]]
    length = len(nums)
    obj = Solution()
    for i in range(length):
        print("nums[", i + 1, "]", " -> ", obj.insert(nums[i], newNums[i]))


if __name__ == "__main__":
    main()
