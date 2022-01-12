#include "Solution.h"

void print(vector<string> res)
{
    int n = res.size();
    cout << "[";
    for (int i = 0; i < n; i++)
    {
        cout << "\"" << res.at(i);
        if (i != n - 1)
            cout << "\",";
        else
            cout << "\"";
    }
    cout << "]" << endl;
}

int main()
{
    string digits = "23";
    Solution Obj;
    vector<string> res = Obj.letterCombinations(digits);
    print(res);
    return 0;
}
/*
Runtime: 0 ms, faster than 100.00% of C++ online submissions for Letter Combinations of a Phone Number.
Memory Usage: 7 MB, less than 34.50% of C++ online submissions for Letter Combinations of a Phone Number.
*/