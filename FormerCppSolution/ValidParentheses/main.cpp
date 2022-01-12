#include "Solution.h"

void display(bool res)
{
    if (res)
        cout << "TRUE" << endl;
    else
        cout << "FALSE" << endl;
}

int main()
{
    string str1 = "()[]{}";
    string str2 = "(]";
    string str3 = "()";
    Solution Obj;
    bool res1 = Obj.isValid(str1);
    bool res2 = Obj.isValid(str2);
    bool res3 = Obj.isValid(str3);
    display(res1);
    display(res2);
    display(res3);

    return 0;
}
// stack
/*
Runtime: 4 ms, faster than 17.27% of C++ online submissions for Valid Parentheses.
Memory Usage: 6.7 MB, less than 76.67% of C++ online submissions for Valid Parentheses.
*/