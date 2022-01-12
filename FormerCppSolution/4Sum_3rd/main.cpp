#include "Solution.h"

// bool operator!=(vector<int> &a, vector<int> &b)
// {
//     int n = a.size();
//     for (int i = 0; i < n; i++)
//         if (a.at(i) != b.at(i))
//             return true;
//     return false;
// }

void print(vector<vector<int>> &res)
{
    cout << "**************************" << endl;
    int n = res.size(), m;
    for (int i = 0; i < n; i++)
    {
        cout << endl;
        cout << "[";
        m = res.at(i).size();
        for (int j = 0; j < m; j++)
        {
            cout << "\"" << res.at(i).at(j) << "\"";
            if (j != m - 1)
                cout << " , ";
        }
        cout << "]" << endl;
    }
    cout << "count = " << n << endl;
    cout << "**************************" << endl;
}

int main()
{
    vector<int> nums1 = {1, 0, -1, 0, -2, 2};
    vector<int> nums2 = {-1, 0, 1, 2};
    vector<int> nums3 = {-2, -1, -1, 1, 1, 2, 2};
    vector<int> nums4 = {0, 4, -5, 2, -2, 4, 2, -1, 4};
    vector<int> nums5 = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    vector<int> nums6 = {-1, 0, 1, 2, -1, -4};
    vector<int> nums7 = {-5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5};
    Solution Obj;
    int target1 = 0;
    int target2 = 2;
    int target3 = 0;
    int target4 = 12;
    int target5 = 0;
    int target6 = -1;
    int target7 = 0;
    vector<vector<int>> res1 = Obj.fourSum(nums1, target1);
    vector<vector<int>> res2 = Obj.fourSum(nums2, target2);
    vector<vector<int>> res3 = Obj.fourSum(nums3, target3);
    vector<vector<int>> res4 = Obj.fourSum(nums4, target4);
    vector<vector<int>> res5 = Obj.fourSum(nums5, target5);
    vector<vector<int>> res6 = Obj.fourSum(nums6, target6);
    vector<vector<int>> res7 = Obj.fourSum(nums7, target7);
    print(res1);
    print(res2);
    print(res3);
    print(res4);
    print(res5);
    print(res6);
    print(res7);
    return 0;
}
/*
Runtime: 164 ms, faster than 18.46% of C++ online submissions for 4Sum.
Memory Usage: 13.7 MB, less than 37.14% of C++ online submissions for 4Sum.
*/