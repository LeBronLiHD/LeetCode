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
    vector<vector<int>> threeSum(vector<int> &nums, int target);
    Solution operator==(vector<int> &b);
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
    if (nums.size() <= 3)
        return {};
    sort(nums.begin(), nums.end());
    int n = nums.size();
    int sum, index = 0;
    vector<vector<int>> res, res_ele;
    vector<int> res_temp;
    for (int i = 0; i < n - 3; i++) // i 仅仅表示次数，无其他意义
    {
        sum = target - nums.at(0);
        nums.erase(nums.begin()); // 在进入 3Sum 前，去除头元素
        res_ele = threeSum(nums, sum);
        if (res_ele.size())
        {
            for (int ii = 0; ii < res_ele.size(); ii++)
            {
                // vector<vector<int>>::iterator it = find(res.begin(), res.end(), res_ele.at(ii));
                res_temp.push_back(target - sum);
                for (int idx = 0; idx < res_ele.at(ii).size(); idx++)
                    res_temp.push_back(res_ele.at(ii).at(idx));

                vector<vector<int>>::iterator it = find(res.begin(), res.end(), res_temp);
                if (res.empty() || it == res.end()) // 去除重复元素
                {
                    res.push_back(res_temp);
                    index++;
                }

                res_temp.clear(); // clear
            }
        }
        // n = nums.size();
    }
    return res;
}

vector<vector<int>> Solution::threeSum(vector<int> &nums, int target) // 3Sum
{
    if (nums.size() <= 2)
        return {};
    vector<vector<int>> res;
    int n = nums.size(), i = 0;
    int sum, front, rear, temp, tempFront, tempRear;

    for (int i = 0; i < n - 2; i++)
    {
        sum = target - nums.at(i);
        front = i + 1;
        rear = n - 1;
        while (rear > front)
        {
            tempFront = nums.at(front);
            tempRear = nums.at(rear);
            temp = tempFront + tempRear;
            if (temp < sum)
            {
                while (front < rear && nums.at(front) == tempFront)
                {
                    front++;
                }
            }
            else if (temp > sum)
            {
                while (front < rear && nums.at(rear) == tempRear)
                {
                    rear--;
                }
            }
            else
            {
                res.push_back({nums.at(i), tempFront, tempRear});
                while (front < rear && nums.at(front) == tempFront)
                {
                    front++;
                }
                while (front < rear && nums.at(rear) == tempRear)
                {
                    rear--;
                }
            }
        }
    }
    return res;
}