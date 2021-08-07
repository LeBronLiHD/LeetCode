# -*- coding: utf-8 -*-
# Runtime: 32 ms, faster than 60.51% of Python3 online submissions for Pow(x, n).
# Memory Usage: 14.1 MB, less than 94.08% of Python3 online submissions for Pow(x, n).

import math


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ret = math.pow(x, n)
        # ret = '%.6f' % ret
        ret = format(ret, ".6f")
        return float(ret)

def main():
    obj = Solution()


if __name__ == "__main__":
    main()
