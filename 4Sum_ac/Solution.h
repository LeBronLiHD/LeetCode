#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
private:
    /* data */
public:
    Solution(/* args */);
    ~Solution();
    vector<vector<int>> fourSum(vector<int> &nums, int target);
    vector<vector<int>> kSum(vector<int> &nums, int start, int k, int target);
    vector<vector<int>> twoSum(vector<int> &nums, int start, int target);
};

Solution::Solution(/* args */)
{
    cout << "constructor called" << endl;
}

Solution::~Solution()
{
    cout << "destructor called" << endl;
}

vector<vector<int>> Solution::fourSum(vector<int> &nums, int target)
{
    sort(nums.begin(), nums.end());
    return kSum(nums, 0, 4, target);
}

vector<vector<int>> Solution::kSum(vector<int> &nums, int start, int k, int target)
{
    vector<vector<int>> res;
    if (start == nums.size() || nums.at(start) * k > target || k * nums.back() < target)
        return res;
    if (k == 2)
        return twoSum(nums, start, target);
    else
        for (int i = start; i < nums.size(); i++)
            if (i == start || nums.at(i - 1) != nums.at(i))
                for (auto &set : kSum(nums, i + 1, k - 1, target - nums.at(i)))
                {
                    res.push_back({nums.at(i)}); // 轮询 k-1 次得到的所有和值（4->3->2）
                    res.back().insert(res.back().end(), set.begin(), set.end());
                }
    return res;
}

vector<vector<int>> Solution::twoSum(vector<int> &nums, int start, int target)
{
    vector<vector<int>> res;
    int front = start, rear = nums.size() - 1, sum;
    while (front < rear)
    {
        sum = nums.at(front) + nums.at(rear);
        if (sum < target)
        {
            front++;
            while (nums.at(front) == nums.at(front - 1) && front < rear)
            {
                front++;
            }
        }
        else if (sum > target)
        {
            rear--;
            while (nums.at(rear) == nums.at(rear + 1) && front < rear)
            {
                rear--;
            }
        }
        else
        {
            res.push_back({nums.at(front++), nums.at(rear--)});
            while (nums.at(front) == nums.at(front - 1) && front < rear)
            {
                front++;
            }
            while (nums.at(rear) == nums.at(rear + 1) && front < rear)
            {
                rear--;
            }
        }
    }
    return res;
}