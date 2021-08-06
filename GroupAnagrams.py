# -*- coding: utf-8 -*-
# 111/114
# Time Limit Exceeded

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        size = len(strs)
        ret = []
        for i in range(size):
            find_class = False
            ans_size = len(ret)
            for j in range(ans_size):
                if self.same_str(ret[j][0], strs[i]):
                    ret[j].append(strs[i])
                    find_class = True
            if find_class == False:
                temp_ret = []
                temp_ret.append(strs[i])
                ret.append(temp_ret)
        return ret


    def same_str(self, str_1, str_2):
        alphabet_1 = {}
        alphabet_2 = {}
        size_1 = len(str_1)
        for i in range(size_1):
            if str_1[i] in alphabet_1:
                alphabet_1[str_1[i]] += 1
            else:
                alphabet_1[str_1[i]] = 1
        size_2 = len(str_2)
        for i in range(size_2):
            if str_2[i] in alphabet_2:
                alphabet_2[str_2[i]] += 1
            else:
                alphabet_2[str_2[i]] = 1
        if len(alphabet_1) != len(alphabet_2):
            return False
        for i in range(size_1):
            if str_1[i] not in alphabet_2:
                return False
            elif alphabet_1[str_1[i]] != alphabet_2[str_1[i]]:
                return False
        return True


def main():
    obj = Solution()
    strs = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        ["aaa"],
        [""]
    ]
    size = len(strs)
    for i in range(size):
        print(obj.groupAnagrams(strs[i]))


if __name__ == "__main__":
    main()
