#include "sulo.h"

int main()
{
    vector<string> str1 = {"flower","flow","flight"};
    vector<string> str2 = {"dog","racecar","car"};
    vector<string> str3 = {""};
    vector<string> str4 = {"a"};
    Solution Obj;
    cout << "    " << Obj.longestCommonPrefix(str1) << endl;
    cout << "    " << Obj.longestCommonPrefix(str2) << endl;
    cout << "    " << Obj.longestCommonPrefix(str3) << endl;
    cout << "    " << Obj.longestCommonPrefix(str4) << endl;
    return 0;
}

/*
Runtime: 4 ms, faster than 94.50% of C++ online submissions for Longest Common Prefix.
Memory Usage: 9.4 MB, less than 81.41% of C++ online submissions for Longest Common Prefix.
*/