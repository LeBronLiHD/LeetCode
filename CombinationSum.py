# -*- coding: utf-8 -*-

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        final_ans_list = []

        if target == 0 or min(candidates) > target:
            return final_ans_list

        size = len(candidates)

        for i in range(size):
            temp = []
            if candidates[i] == target:
                temp.append(candidates[i])
                final_ans_list.append(temp)

        for i in range(size):
            if candidates[i] < target:
                # temp_candidates = []
                # for j in range(size):
                #     if j != i:
                #         temp_candidates.append(candidates[j])
                ans_list = self.combinationSum(candidates, target - candidates[i])
                size_ans = len(ans_list)  # List[List[int]]
                if size_ans == 0:
                    continue
                for i_ans in range(size_ans):
                    temp = []
                    temp = ans_list[i_ans]
                    temp.append(candidates[i])
                    final_ans_list.append(temp)
        return final_ans_list


def main():
    obj = Solution()
    target = 7
    candidates = [2, 3, 6, 7]
    ans_list = obj.combinationSum(candidates, target)
    print(ans_list)


if __name__ == "__main__":
    main()
