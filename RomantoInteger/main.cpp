#include "roman.h"

int main()
{
    string s = "MCMXCIV";
    Solution Obj;
    // string test = "M";
    // cout << "    " << test.compare(0, test.size(), s, 0, test.size()) << endl;
    int res = Obj.romanToInt(s);
    cout << "    " << res << endl;
    return 0;
}
/*
Runtime: 4 ms, faster than 92.57% of C++ online submissions for Roman to Integer.
Memory Usage: 6.4 MB, less than 68.83% of C++ online submissions for Roman to Integer.
*/