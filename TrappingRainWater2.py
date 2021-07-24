# -*- coding: utf-8 -*-
# At any position amount of water that can be trapped = min (max left height, max right height) - own height
# Runtime: 56 ms, faster than 16.39% of Python online submissions for Trapping Rain Water.
# Memory Usage: 14 MB, less than 97.07% of Python online submissions for Trapping Rain Water.

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
        max_left = [0] * size
        max_right = [0] * size
        max_left[0] = height[0]
        max_right[-1] = height[-1]
        for i in range(1, size - 1):
            max_left[i] = max(max_left[i - 1], height[i])
            max_right[-i - 1] = max(max_right[-i], height[-i - 1])
        for i in range(1, size - 1):
            if min(max_left[i], max_right[i]) > height[i]:
                trap += min(max_left[i], max_right[i]) - height[i]
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
