# -*- coding: utf-8 -*-
# Runtime: 16 ms, faster than 75.53% of Python online submissions for Length of Last Word.
# Memory Usage: 14.1 MB, less than 5.76% of Python online submissions for Length of Last Word.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        for i in range(size - 1, -1, -1):
            if s[i] != ' ':
                pre_i = i
                while i >= 0 and s[i] != ' ':
                    i -= 1
                return pre_i - i
        return 0


def main():
    nums = ["Hello World",
            "   fly me   to   the moon  ",
            "luffy is still joyboy"]
    length = len(nums)
    obj = Solution()
    for i in range(length):
        print("array[", i + 1, "]", " -> ", obj.lengthOfLastWord(nums[i]))


if __name__ == "__main__":
    main()
