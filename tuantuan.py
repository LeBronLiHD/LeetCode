# -*- coding: utf-8 -*-


if __name__ == "__main__":
    board = ["TUAN", "tuan", "TUAN", "tuan"]
    ans = []
    ans.append(["".join(row) for row in board])
    board = ["LALA", "lala", "LALA", "lala"]
    ans.append(["".join(row) for row in board])
    print(ans)
    nums = [i for i in range(11)]
    print(nums)
    size = len(nums)
    print(nums[0:int(size/2)])
    print(nums[int(size/2):size])
    matrix = [1, 2, 3]
    matrix.append([4, 5, 6])
    matrix += [4, 5, 6]
    print(matrix)
    matrix.remove(matrix[3])
    print(matrix)
    one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    two = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(one + two[1:len(two)])
