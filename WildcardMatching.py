# -*- coding: utf-8 -*-
# 1708 / 1811 test cases passed. time limit exceeded

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        size_p = len(p)
        size_s = len(s)
        if size_p == 0 and size_s == 0:
            return True

        i_s = 0
        i_p = 0
        while i_p < size_p and i_s < size_s:
            if p[i_p] != '*':
                if p[i_p] == '?' or p[i_p] == s[i_s]:
                    i_p += 1
                    i_s += 1
                    continue
                else:
                    return False
            else:
                while p[i_p] == '*':
                    if i_p == size_p - 1:
                        return True
                    i_p += 1
                while i_s < size_s:
                    if p[i_p] == s[i_s] or p[i_p] == '?':
                        if self.isMatch(s[i_s:size_s], p[i_p:size_p]):
                            return True
                    i_s += 1
                return False

        if i_p == size_p and i_s == size_s:
            return True
        elif i_p < size_p:
            for i in range(i_p, size_p):
                if p[i] != '*':
                    return False
            return True
        else:
            return False


def main():
    obj = Solution()
    s = ["aa",
         "adceb",
         "acdcb",
         "lihaodong",
         "aaa",
         "",
         "",
         "a",
         "lihaodongnbnbnbnbtuantuantuantuasntusnrdfbadfetgsdfvbrtgasddfwerafdasdfasdfasdfasdcascasdc"]
    p = ["a",
         "*a*b",
         "a*c?b",
         "lihaodong",
         "aaaaaa",
         "**********************",
         "",
         "*?*****************",
         "*c*********************************************************************************c*c**"]
    size = len(s)
    for i in range(size):
        answer = obj.isMatch(s[i], p[i])
        if answer:
            print(" <", i, "> is True")
        else:
            print(" <", i, "> is False")
    # '?' Matches any single character.
    # '*' Matches any sequence of characters (including the empty sequence).


if __name__ == "__main__":
    main()

'''
1. simple
    1. if no '*', just compare if they are equal or not
    2. else, cut the string s and compare
2. stack(recursion)
    1. just compare
'''
