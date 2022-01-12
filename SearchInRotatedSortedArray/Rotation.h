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
    // for (vector<int>::iterator it = nums.begin(); it < nums.end(); it++)
    // {
    //     if (target == (*it))
    //         return 99;
    // }
    int size = nums.size();
    for (int i = 0; i < size; i++)
    {
        if (target == nums.at(i))
            return i;
    }
    return -1;
}

Rotation::~Rotation()
{
}
