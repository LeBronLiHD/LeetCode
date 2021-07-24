# -*- coding: utf-8 -*-
# recursion with memory
# Runtime: 732 ms, faster than 64.97% of Python3 online submissions for Wildcard Matching.
# Memory Usage: 110.8 MB, less than 18.81% of Python3 online submissions for Wildcard Matching.

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        if p[i_p] == '?' or s[i_s] == p[i_p]:
            return self.isMatch(s[0, size_s - 1], p[0, size_p - 1])
        elif p[i_p] == '*':
            return self.isMatch(s[0, size_s - 1], p[0, size_p]) or \
                   self.isMatch(s[0, size_s], p[0, size_p - 1])
        else:
            return False
        """
        memory = {}
        
        def match(i, j):
            nonlocal memory
            if (i, j) in memory:
                return memory[(i, j)]

            if i >= len(s) and j >= len(p):
                return True
            elif i >= len(s):
                if p[j] == '*':
                    memory[(i, j)] = match(i, j + 1)
                else:
                    memory[(i, j)] = False
            elif j >= len(p):
                return False
            else:
                if p[j] == '?' or p[j] == s[i]:
                    memory[(i, j)] = match(i + 1, j + 1)
                elif p[j] == '*':
                    plus = 0
                    size = len(p)
                    while j + plus < size and p[j + plus] == '*':
                        plus += 1
                    plus -= 1
                    memory[(i, j)] = match(i, j + 1 + plus) or match(i + 1, j + plus)
                else:
                    memory[(i, j)] = False

            return memory[(i, j)]

        return match(0, 0)


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

