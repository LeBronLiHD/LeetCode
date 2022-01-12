#include <iostream>
#include "main.h"
#define N 9
using namespace std;

typedef int height[N];

int main(int argc, char *argv)
{
    Solution<vector<int>> Obj;
    height test = { 1, 8, 6, 2, 5, 4, 8, 3, 7 };
    int contain = Obj.maxArea(test);
    cout << "    " << contain;
    return 0;
}