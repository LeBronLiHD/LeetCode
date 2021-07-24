# -*- coding: utf-8 -*-
# dynamic programing
# Runtime: 764 ms, faster than 57.81% of Python online submissions for Wildcard Matching.
# Memory Usage: 22.8 MB, less than 17.30% of Python online submissions for Wildcard Matching.

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ss, sp = len(s), len(p)
        if ss == 0 and sp == 0:
            return True
        elif sp == 0:
            return False
        elif ss == 0:
            for i in range(sp):
                if p[i] != '*':
                    return False
            return True
        dp = []
        for i in range(sp + 1):
            row = []
            for j in range(ss + 1):
                row.append(0)
            dp.append(row)
        dp[sp][ss] = 1
        ptr_s = ss
        for i_p in range(sp - 1, -1, -1):
            changed = 0
            for i_s in range(ss - 1, -1, -1):
                if p[i_p] == '*':
                    flag = False
                    for i in range(ss + 1):
                        if dp[i_p + 1][i] == 1:
                            flag = True
                            break
                    if flag:
                        for i in range(ptr_s + 1):
                            dp[i_p][i] = 1
                        break
                    else:
                        return False
                if dp[i_p + 1][i_s + 1] == 1 and dp[i_p][i_s] == 0:
                    if p[i_p] == '?' or p[i_p] == s[i_s]:
                        dp[i_p][i_s] = 1
                        if changed == 0:
                            ptr_s = i_s
                            changed += 1
        return dp[0][0] == 1


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

