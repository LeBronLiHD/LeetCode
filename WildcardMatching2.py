# -*- coding: utf-8 -*-
# recursion 1701 / 1811 test cases passed. Time limit exceeded

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        size_p = len(p)
        size_s = len(s)
        '''
        if p[i_p] == '?' or s[i_s] == p[i_p]:
            return self.isMatch(s[0, size_s - 1], p[0, size_p - 1])
        elif p[i_p] == '*':
            return self.isMatch(s[0, size_s - 1], p[0, size_p]) or \
                   self.isMatch(s[0, size_s], p[0, size_p - 1])
        else:
            return False
        '''
        if size_p == 0 and size_s == 0:
            return True
        elif size_s == 0:
            if p[-1] == '*':
                return self.isMatch(s, p[0:size_p - 1])
            else:
                return False
        elif size_p == 0:
            return False
        else:
            if p[-1] == '?' or s[-1] == p[-1]:
                return self.isMatch(s[0:size_s - 1], p[0:size_p - 1])
            elif p[-1] == '*':
                i2 = size_p - 1
                while i2 >= 0 and p[i2] == '*':
                    i2 -= 1
                if i2 < 0:
                    return True
                for i3 in range(size_s):
                    if self.isMatch(s[0:size_s - i3], p[0:i2 + 1]):
                        return True
                return self.isMatch(s[0:size_s - 1], p[0:i2 + 2])
            else:
                return False


def main():
    obj = Solution()
    s = ["ab",
         "adceb",
         "acdcb",
         "lihaodong",
         "aaa",
         "",
         "",
         "aaaaaaaaaaa",  # 1
         "abc",
         "abaabaaaabbabbaaabaabababbaabaabbabaaaaabababbababaabbabaabbbbaabbbbbbbabaaabbaaaaabbaabbbaaaaabbbabb",
         "aaabaabaaaaabbabaabababbbbaabbabbaabbbbbbbbbaaaaabaa",
         "aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba",
         "abbabbbaabaaabbbbbabbabbabbbabbaaabbbababbabaaabbab",
         "cdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddc",
         "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb"]
    p = ["*?*?*",
         "*a*b",
         "a*c?b",
         "*",
         "aaaaaa",
         "**********************",
         "",
         "???",  # 1
         "*?*?*?*",
         "ab*aaba**abbaaaa**b*b****aa***a*b**ba*a**ba*baaa*b*ab*",
         "b****a**b*aab******b**aa",
         "*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*",
         "*aabb***aa**a******aa*",  # True
         "*c*********************************************************************************c*c**",
         "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"]
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

