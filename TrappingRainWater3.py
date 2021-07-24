# -*- coding: utf-8 -*-
# At any position amount of water that can be trapped = min (max left height, max right height) - own height
# Runtime: 56 ms, faster than 16.39% of Python online submissions for Trapping Rain Water.
# Memory Usage: 14.2 MB, less than 61.97% of Python online submissions for Trapping Rain Water.

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)
        if size == 0:
            return 0
        trap = 0
        right_height = []
        left_max = height[0]
        right_max = max(height)
        for i in range(size):
            right_height.append(height[i])
        right_height.append(0)
        for i in range(size):
            right_height.pop(0)
            if height[i] >= right_max:
                right_max = max(right_height)
            if i > 0:
                left_max = max(height[i - 1], left_max)
            if min(left_max, right_max) > height[i]:
                trap += min(left_max, right_max) - height[i]
        return trap


def main():
    obj = Solution()
    height = [[4, 2, 0, 3, 2, 5],
              [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
              [0, 1, 2, 3, 2, 1, 0],
              [0, 1, 2, 3, 4, 0, 4, 3, 2, 1, 0],
              []]
    size = len(height)
    for i in range(size):
        print("trap of height <", i, "> is ", obj.trap(height[i]))


if __name__ == "__main__":
    main()
