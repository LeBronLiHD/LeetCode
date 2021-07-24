# -*- coding: utf-8 -*-
# Runtime: 20 ms, faster than 80.61% of Python online submissions for Multiply Strings.
# Memory Usage: 13.7 MB, less than 21.92% of Python online submissions for Multiply Strings.
# Runtime: 28 ms, faster than 56.69% of Python online submissions for Multiply Strings.
# Memory Usage: 13.4 MB, less than 78.29% of Python online submissions for Multiply Strings.

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) * int(num2))
        # A, B = 0, 0
        # for i in num1:
        #     A = A * 10 + ord(i) - ord('0')
        # for j in num2:
        #     B = B * 10 + ord(j) - ord('0')
        # return str(A * B)


def main():
    obj = Solution()
    print("123456789 * 456789123 = ", obj.multiply("123456789", "456789123"))


if __name__ == "__main__":
    main()
