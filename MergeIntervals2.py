# -*- coding: utf-8 -*-
# Runtime: 150 ms, faster than 5.08% of Python online submissions for Merge Intervals.
# Memory Usage: 15.6 MB, less than 97.25% of Python online submissions for Merge Intervals.

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        def intervalsSort(leftIndex, rightIndex):
            if rightIndex - leftIndex == 0:
                return [intervals[leftIndex]]
            if rightIndex - leftIndex == 1:
                if intervals[leftIndex][0] <= intervals[rightIndex][0]:
                    return [intervals[leftIndex], intervals[rightIndex]]
                else:
                    return [intervals[rightIndex], intervals[leftIndex]]
            midIndex = (leftIndex + rightIndex) // 2
            leftList = intervalsSort(leftIndex, midIndex)
            rightList = intervalsSort(midIndex + 1, rightIndex)
            ansList = []
            i, j = 0, 0
            while i < len(leftList) and j < len(rightList):
                if leftList[i][0] >= rightList[j][0]:
                    ansList.append(rightList[j])
                    j += 1
                else:
                    ansList.append(leftList[i])
                    i += 1
            if i < len(leftList):
                ansList += leftList[i:len(leftList)]
            if j < len(rightList):
                ansList += rightList[j:len(rightList)]
            return ansList

        # intervals.sort(key=lambda x: x[0])
        size = len(intervals)
        intervals = intervalsSort(0, size - 1)
        # print(intervals)
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
