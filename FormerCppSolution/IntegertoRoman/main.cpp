#include <iostream>
// #include <string>
#include "roman.h"
using namespace std;

int main()
{
    int int1 = 1994;
    int int3 = 9;
    int int4 = 58;

    Solution Obj;
    string roman = Obj.intToRoman(int1);
    cout << "    " << roman;
    return 0;
}

/*
Runtime: 16 ms, faster than 31.27% of C++ online submissions for Integer to Roman.
Memory Usage: 6.2 MB, less than 92.12% of C++ online submissions for Integer to Roman.
*/