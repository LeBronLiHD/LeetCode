# -*- coding: utf-8 -*-
# Runtime: 48 ms, faster than 93.64% of Python3 online submissions for Wildcard Matching.
# Memory Usage: 14.1 MB, less than 99.42% of Python3 online submissions for Wildcard Matching.

class Solution(object):
    def isMatch(self, s, p) -> bool:
        size = len(s)
        size_p = len(p)
        i, j, last_p_index, last_s_index = 0, 0, -1, 0
        while i < size:
            if j < size_p and (s[i] == p[j] or p[j] in {s[i], '?'}):
                i += 1
                j += 1
            elif j < size_p and p[j] == '*':
                last_p_index = j  # last passed index of p
                j += 1  # move to the next index, which is either letter in lower case or null
                last_s_index = i  # last passed index of s
            elif last_p_index >= 0:
                j = last_p_index  # back to former situation, such as p = "*a", s = "aaa"
                last_s_index += 1  # if not go into the first `if`, means the '*' covered it s++ and update last_s_index
                i = last_s_index
            else:
                return False
        while j < size_p and p[j] == '*':
            j += 1
        return j == size_p


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

'''
1. if no '*', simple compare and i++, j++
2. if we got '*', move ptr_p to the next unit (remember last_p_index and last_s_index)
    1. if p is empty, just move ptr_s until s is empty
    2. if p is not empty, move ptr_p until p is not '*'
        1. if equal, must at least 1 s equal to p
            1. if the number matches is 1 and passed, just continue
            2. if the last match failed, back ptr_p to init position without backing ptr_s 
               (let the last '*' cover the current position of s), continue
        2. if s is over and no char matches p, return False
'''
