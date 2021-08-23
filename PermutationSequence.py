# -*- coding: utf-8 -*-
# Runtime: 16 ms, faster than 83.40% of Python online submissions for Permutation Sequence.
# Memory Usage: 13.4 MB, less than 49.01% of Python online submissions for Permutation Sequence.
# Runtime: 20 ms, faster than 62.45% of Python online submissions for Permutation Sequence.
# Memory Usage: 13.2 MB, less than 92.09% of Python online submissions for Permutation Sequence.

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numberList = [i for i in range(1, n + 1)]
        # print("numberList -> ", numberList)
        Factorial = []
        curValue = 1
        for i in range(1, n + 1):
            curValue *= i
            Factorial.append(curValue)
        # print("Factorial -> ", Factorial)
        ansString = ""
        k -= 1
        for i in range(1, n):
            curNumberIndex = int(k/Factorial[n - i - 1])
            curNumber = numberList[curNumberIndex]
            ansString += str(curNumber)
            numberList.remove(curNumber)
            k -= curNumberIndex * Factorial[n - i - 1]
            if k < 0:
                k += n
        ansString += str(numberList[0])
        return ansString


def main():
    nums = [[3, 3],
            [4, 9],
            [9, 25],
            [6, 6],
            [25, 100]]
    size = len(nums)
    obj = Solution()
    for i in range(size):
        print("nums[", i, "] -> ", nums[i], " -> ", obj.getPermutation(nums[i][0], nums[i][1]))


if __name__ == '__main__':
    main()

'''
for number 4:
1 2 3 4
1 2 4 3
1 3 2 4
1 3 4 2
1 4 2 3
1 4 3 2
2 1 3 4
2 1 4 3
2 3 1 4 [9]
2 3 4 1
...
'''
