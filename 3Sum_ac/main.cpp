#include "Solution.h"

void print(vector<vector<int>> res)
{
    for (int i = 0; i != res.size(); i++)
    {
        for (auto j = res.at(i).begin(); j != res.at(i).end(); j++)
            cout << " " << *j << " ";
        cout << endl;
    }
}

int main()
{
    vector<int> nums1 = {-1, 0, 1, 2, -1, -4};
    vector<int> nums2 = {};
    vector<int> nums3 = {0, 0, 0, 0, 0};
    vector<int> nums4 = {-1, 0, 1, 0};
    Solution Obj;
    vector<vector<int>> res1 = Obj.threeSum(nums1);
    vector<vector<int>> res2 = Obj.threeSum(nums2);
    vector<vector<int>> res3 = Obj.threeSum(nums3);
    vector<vector<int>> res4 = Obj.threeSum(nums4);

    print(res1);
    print(res2);
    print(res3);
    print(res4);

    return 0;
}
/*
Runtime: 92 ms, faster than 66.81% of C++ online submissions for 3Sum.
Memory Usage: 20.5 MB, less than 67.02% of C++ online submissions for 3Sum.
*/