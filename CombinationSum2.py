# -*- coding: utf-8 -*-

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if target == 0 or min(candidates) > target:
            return []

        final_ans_list = []
        candidates.sort()
        size = len(candidates)

        for i in range(size):
            temp = []
            if target == candidates[i]:
                temp.append(candidates[i])
                final_ans_list.append(temp)
                break

        for i in range(size):
            if candidates[i] < target:
                temp_candidate = []
                for j in range(size - i):
                    temp_candidate.append(candidates[j + i])
                ans_list = self.combinationSum(temp_candidate, target - candidates[i])
                ans_size = len(ans_list)
                if ans_size == 0:
                    continue
                for j in range(ans_size):
                    temp = []
                    temp = ans_list[j]
                    temp.append(candidates[i])
                    final_ans_list.append(temp)
            else:
                break
        return final_ans_list


def main():
    obj = Solution()
    target = [7, 8, 1, 2, 9]
    candidates = [[2, 3, 7, 6],
                  [2, 3, 5],
                  [2],
                  [1],
                  [9]]
    size = len(target)
    for i in range(size):
        ans_list = obj.combinationSum(candidates[i], target[i])
        print(ans_list)


if __name__ == "__main__":
    main()
