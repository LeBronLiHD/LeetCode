# -*- coding: utf-8 -*-
# button down dynamic programing
# Runtime: 1048 ms, faster than 32.70% of Python online submissions for Wildcard Matching.
# Memory Usage: 21.5 MB, less than 62.03% of Python online submissions for Wildcard Matching.

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ss, sp = len(s), len(p)
        dp = [[0]*(ss + 1) for _ in range(sp + 1)]
        dp[0][0] = 1
        for i in range(sp):
            if p[i] == '*':
                dp[i + 1][0] = 1
            else:
                break
        for i_p in range(sp):
            for i_s in range(ss):
                if p[i_p] == '?' or p[i_p] == s[i_s]:
                    dp[i_p + 1][i_s + 1] = dp[i_p][i_s]
                if p[i_p] == '*':
                    dp[i_p + 1][i_s + 1] = max(dp[i_p + 1][i_s], dp[i_p][i_s + 1])
        return dp[-1][-1] == 1


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

