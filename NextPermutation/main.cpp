#include "permutation.h"

int main()
{
    permutation Obj;
    vector<int> nums = {1, 5, 1};
    Obj.nextPermutation(nums);
    Obj.printAns(nums);
    return 0;
}