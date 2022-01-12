#include <iostream>
#include <vector>
using namespace std;

class permutation
{
private:
public:
    permutation();
    ~permutation();
    void nextPermutation(vector<int> &nums);
    void printAns(vector<int> &nums);
    void reserve(vector<int> &nums, int begin, int end);
    void swap(vector<int> &nums, int left, int right);
};

permutation::permutation()
{
    cout << "constructor called" << endl;
}

void permutation::nextPermutation(vector<int> &nums)
{
    // Find the largest index k such that nums[k] < nums[k + 1].
    // If no such index exists, just reverse nums and done.
    //
    // Find the largest index l > k such that nums[k] < nums[l].
    // Swap nums[k] and nums[l]. Reverse the sub-array nums[k + 1:].
    int index = -1;
    int size = nums.size();
    for (size_t i = size - 1; i >= 1; i--)
    {
        if (nums.at(i - 1) < nums.at(i))
        {
            index = i - 1;
            break;
        }
    }
    if (index < 0)
    {
        reserve(nums, 0, size - 1);
        return;
    }
    else
    {
        int temp = nums.at(index);
        for (size_t i = size - 1; i >= 0; i--)
        {
            if (nums.at(i) > temp)
            {
                swap(nums, index, i);
                reserve(nums, index + 1, size - 1);
                return;
            }
        }
        swap(nums, index, 0);
        reserve(nums, index + 1, size - 1);
        return;
    }
    cout << "ERROR" << endl;
}

void permutation::printAns(vector<int> &nums)
{
    cout << "calculation done!" << endl;
    for (size_t i = 0; i < nums.size() - 1; i++)
    {
        cout << " " << nums.at(i) << " ->";
    }
    cout << " " << nums.at(nums.size() - 1) << endl;
}

void permutation::reserve(vector<int> &nums, int begin, int end)
{
    while (end > begin)
    {
        swap(nums, begin, end);
        begin++;
        end--;
    }
}

void permutation::swap(vector<int> &nums, int left, int right)
{
    int temp = nums.at(left);
    nums.at(left) = nums.at(right);
    nums.at(right) = temp;
}

permutation::~permutation()
{
    cout << "destructor called" << endl;
}
