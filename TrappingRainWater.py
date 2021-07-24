# -*- coding: utf-8 -*-
# 319 / 320 test cases passed.
# time limit exceeded

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)
        if size == 0:
            return 0
        max_height = height[0]
        for i in range(size):
            if height[i] > max_height:
                max_height = height[i]
        count_num = []
        count_index = []
        for i in range(max_height + 1):
            count_num.append(0)
            temp_list = []
            count_index.append(temp_list)
        mountain = []
        sum_height = 0
        for i in range(size):
            mountain.append(height[i])
            sum_height += height[i]
            for j in range(height[i] + 1):
                count_index[j].append(i)
                count_num[j] += 1
        for i in range(max_height, 0, -1):
            if count_num[i] >= 2:
                for j in range(count_index[i][0], count_index[i][count_num[i] - 1] + 1):
                    if i > mountain[j]:
                        mountain[j] = i
            else:
                continue
        sum_count = 0
        for i in range(size):
            sum_count += mountain[i]
        return sum_count - sum_height


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

'''
1. build a list after raining, calculate the sum of the two list, and the sub answer is trap
2. dynamic programing, build a two dimension matrix
3. define left_height and right_height, two count the trap of rain
4. count the height unit and build mountain list
5. rain from level by level, 0 -> 1 -> 2 -> ...
'''