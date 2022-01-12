#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <stack>
#include <random>

using namespace std;

class FirstAndLast
{
private:
    vector<int> nums;
    int target;

public:
    FirstAndLast(vector<int> N, int T);
    ~FirstAndLast();
    vector<int> searchRange();
    void printAns(vector<int> ans);
};

FirstAndLast::FirstAndLast(vector<int> N, int T) : nums(N), target(T)
{
}

vector<int> FirstAndLast::searchRange()
{
    // we try O(logn) time complexity
    int n = nums.size();
    int lo = 0, hi = n - 1, mi;
    int left = -1, right = -1;
    while (lo <= hi)
    {
        mi = (lo + hi) / 2;
        if (nums.at(mi) > target)
            hi = mi - 1;
        else if (nums.at(mi) < target)
            lo = mi + 1;
        else
        {
            left = right = mi;
            for (int i = mi + 1; i < n; i++)
            {
                if (nums.at(i) == target)
                    right++;
                else
                    break;
            }
            for (int i = mi - 1; i >= 0; i--)
            {
                if (nums.at(i) == target)
                    left--;
                else
                    break;
            }
            break;
        }
    }
    return {left, right};
}

FirstAndLast::~FirstAndLast()
{
}

void FirstAndLast::printAns(vector<int> ans)
{
    cout << "calculation done at " << this << endl;
    int size = ans.size();
    for (int i = 0; i < size - 1; i++)
        cout << " " << ans.at(i) << " ->";
    cout << " " << ans.at(size - 1) << endl;
}
