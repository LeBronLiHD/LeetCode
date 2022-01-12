#include "remove.h"

int main()
{
    vector<int> nums = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    int val;
    cout << endl
         << "enter a value: ";
    cin >> val;
    Remove Obj;
    Obj.display(nums, val);
    return 0;
}