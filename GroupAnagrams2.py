# -*- coding: utf-8 -*-
# Runtime: 96 ms, faster than 77.58% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.9 MB, less than 44.24% of Python3 online submissions for Group Anagrams.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        memory = {}
        ret = []
        for string in strs:
            sorted_string = tuple(sorted(string))
            if sorted_string in memory:
                ret[memory[sorted_string]].append(string)
            else:
                memory[sorted_string] = len(ret)
                ret.append([string])
        return ret


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
