# -*- coding: utf-8 -*-

class Solution(object):
    def combinationSum2(self, candidates, target):
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

        cur_int = candidates[0]
        last_int = -1
        for i in range(size):
            cur_int = candidates[i]
            if candidates[i] < target and cur_int != last_int:
                last_int = cur_int
                temp_candidate = []
                for j in range(size - i):
                    if i + j + 1 < size:
                        temp_candidate.append(candidates[j + i + 1])
                if len(temp_candidate) == 0:
                    continue
                ans_list = self.combinationSum2(temp_candidate, target - candidates[i])
                ans_size = len(ans_list)
                if ans_size == 0:
                    continue
                for j in range(ans_size):
                    temp = []
                    temp = ans_list[j]
                    temp.append(candidates[i])
                    final_ans_list.append(temp)
            else:
                continue
        return final_ans_list


def main():
    obj = Solution()
    target = [8, 5]
    candidates = [[10, 1, 2, 7, 6, 1, 5],
                  [2, 5, 2, 1, 2]]
    size = len(target)
    for i in range(size):
        ans_list = obj.combinationSum2(candidates[i], target[i])
        print(ans_list)


if __name__ == "__main__":
    main()
