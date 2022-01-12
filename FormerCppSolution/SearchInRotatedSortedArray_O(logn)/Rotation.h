#include <iostream>
#include <iomanip>
#include <vector>
#include <stack>
#include <string>
#include <random>
using namespace std;

class Rotation
{
private:
    vector<int> nums;
    int target;

public:
    Rotation(vector<int> N, int T);
    ~Rotation();
    int search();
};

Rotation::Rotation(vector<int> N, int T) : nums(N), target(T)
{
}

int Rotation::search()
{
    // this is an O(logn) algorithm
    // 1. find the pivot index k, the index of the smallest value
    int n = nums.size();
    int lo = 0, hi = n - 1, mi;
    while (lo < hi) // break when lo == hi
    {
        mi = (lo + hi) / 2;
        if (nums.at(mi) > nums.at(hi))
            lo = mi + 1;
        else
            hi = mi; // mi maybe the pivot index
    }
    int pivot = lo;
    lo = 0, hi = n - 1;
    int realIndex;
    while (lo <= hi)
    {
        mi = (lo + hi) / 2;
        realIndex = (mi + pivot) % n; // Pan pivot indexes
        if (nums.at(realIndex) > target)
            hi = mi - 1;
        else if (nums.at(realIndex) < target)
            lo = mi + 1;
        else
            return realIndex;
    }
    return -1;
}

Rotation::~Rotation()
{
}
