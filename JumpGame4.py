# -*- coding: utf-8 -*-
# TODO

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)

        def coveredOrNot(zeroIndex):
            # TODO
            for i in range(zeroIndex - 1, -1, -1):
                if nums[i] == 0:
                    return False
                else:
                    if nums[i] > zeroIndex - i:
                        return True
            return False

        newestZeroIndex = -1
        firstNotCovered = -1
        for i in range(size - 1, -1, -1):
            if nums[i] == 0:
                newestZeroIndex = i
                # TODO: judge if this index could be covered
                # if this index could not be covered, continue
                if coveredOrNot(newestZeroIndex) == False:
                    firstNotCovered = i
                    continue
                else:
                    continue
            else:
                continue
        # now, newestZeroIndex locate the position of the last zero
        # TODO: if this zero could not be covered, return False
        if coveredOrNot(newestZeroIndex) == False:
            return False
        return True


def main():
    obj = Solution()
    nums = [[2, 3, 1, 1, 4],
            [3, 2, 1, 0, 4],
            [1, 2, 3],
            [2, 0, 0],
            [3, 0, 8, 2, 0, 0, 1],
            [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]]
    size = len(nums)
    for i in range(size):
        print(i, " -> ", obj.canJump(nums[i]))


if __name__ == "__main__":
    main()
