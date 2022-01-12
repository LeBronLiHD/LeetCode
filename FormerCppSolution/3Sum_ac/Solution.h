#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution
{
private:
    /* data */
public:
    Solution(/* args */);
    vector<vector<int>> threeSum(vector<int> &nums);
    ~Solution();
};

Solution::Solution(/* args */)
{
    cout << "constructor called" << endl;
}

vector<vector<int>> Solution::threeSum(vector<int> &nums)
{
    sort(nums.begin(), nums.end());
    vector<vector<int>> res = {};
    int n = nums.size();
    int temp, front, rear, sum, F, R;
    for (int i = 0; i < n - 1;)
    {
        temp = 0 - nums.at(i);
        if (temp < 0)
            break;

        front = i + 1;
        rear = n - 1;
        while (front < rear)
        {
            sum = nums.at(front) + nums.at(rear);
            if (sum < temp)
                front++;
            else if (sum > temp)
                rear--;
            else
            {
                F = nums.at(front);
                R = nums.at(rear);
                res.push_back({-temp, F, R});
                while (front < rear && nums.at(front) == F)
                {
                    front++; // at least one time
                }
                while (front < rear && nums.at(rear) == R)
                {
                    rear--;
                }
            }
        }
        while (nums.at(i) == -temp && i < n - 1)
            i++;
    }
    return res;
}

Solution::~Solution()
{
    cout << "deconstructor called" << endl;
}
