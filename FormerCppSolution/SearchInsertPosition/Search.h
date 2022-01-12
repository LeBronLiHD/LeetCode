#include <iostream>
#include <iomanip>
#include <vector>
#include <stack>
#include <random>

using namespace std;

class Search
{
private:
    vector<int> nums;
    int target;

public:
    Search(vector<int> N, int T);
    ~Search();
    int searchInsert();
};

Search::Search(vector<int> N, int T) : nums(N), target(T)
{
}

int Search::searchInsert()
{
    // O(logn)
    int n = nums.size();
    int lo = 0, hi = n - 1, mi;
    while (lo < hi)
    {
        mi = (lo + hi) / 2;
        if (nums.at(mi) > target)
            hi = mi - 1;
        else if (nums.at(mi) < target)
            lo = mi + 1;
        else
            return mi;
    }
    return (nums.at(lo) >= target) ? lo : lo + 1;
}

Search::~Search()
{
}