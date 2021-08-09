# -*- coding: utf-8 -*-
# CallBack
# Runtime: 20 ms, faster than 42.90% of Python online submissions for Spiral Matrix.
# Memory Usage: 13.5 MB, less than 14.49% of Python online submissions for Spiral Matrix.

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def anotherLevel(subMatrix):
            rows = len(subMatrix)
            cols = len(subMatrix[0])
            if rows == 1:
                return subMatrix[0]
            if rows == 2:
                tempAns = subMatrix[0]
                for i in range(cols - 1, -1, -1):
                    tempAns.append(subMatrix[1][i])
                return tempAns
            if cols == 1:
                tempAns = []
                for i in range(rows):
                    tempAns.append(subMatrix[i][0])
                return tempAns
            if cols == 2:
                tempAns = subMatrix[0]
                for i in range(1, rows):
                    tempAns.append(subMatrix[i][1])
                for i in range(rows - 1, 0, -1):
                    tempAns.append(subMatrix[i][0])
                return tempAns
            tempAns = []
            for i in range(cols):
                tempAns.append(subMatrix[0][i])
            for i in range(1, rows):
                tempAns.append(subMatrix[i][cols - 1])
            for i in range(cols - 2, -1, -1):
                tempAns.append(subMatrix[rows - 1][i])
            for i in range(rows - 2, 0, -1):
                tempAns.append(subMatrix[i][0])
            subMatrix = subMatrix[1:rows - 1]
            for i in range(0, rows - 2):
                subMatrix[i] = subMatrix[i][1:cols - 1]
            tempAns += anotherLevel(subMatrix)
            return tempAns
        return anotherLevel(matrix)


def main():
    obj = Solution()
    matrixs = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
               [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
               [[7], [9], [6]],
               [[7, 7], [9, 9], [6, 6]]]
    size = len(matrixs)
    for i in range(size):
        print(i + 1, " -> ", obj.spiralOrder(matrixs[i]))


if __name__ == "__main__":
    main()
