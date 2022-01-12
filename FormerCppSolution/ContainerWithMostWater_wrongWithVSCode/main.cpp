#include <iostream>
#include "max.h"
using namespace std;


int main(int argv, char*argc[])
{
    Solution<vector<int>> Obj;
    vector<int> test;
    test.push_back(1);
    test.push_back(7);
    test.push_back(6);
    test.push_back(2);
    test.push_back(5);
    test.push_back(8);
    test.push_back(4);
    test.push_back(3);
    test.push_back(7);
    test.push_back(1);

    int contain = Obj.maxArea(test);
    cout << "    " << contain;
    return 0;
}
/*
Runtime: 44 ms, faster than 15.14% of C++ online submissions for Container With Most Water.
Memory Usage: 18 MB, less than 93.70% of C++ online submissions for Container With Most Water.
*/