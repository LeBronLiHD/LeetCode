#include <iostream>
#include <vector>
using namespace std;

class Remove
{
private:
public:
    Remove();
    ~Remove();
    int RemoveElement(vector<int> &nums, int val);
    void display(vector<int> &nums, int val);
    friend ostream &operator<<(ostream &output, vector<int> &nums);
};

Remove::Remove()
{
}

int Remove::RemoveElement(vector<int> &nums, int val)
{
    // nums.end() is not the last element, but the element after the last one
    for (vector<int>::iterator it = nums.begin(); it != nums.end(); it++)
    {
        if (val == (*it))
        {
            nums.erase(it);
            it--;
        }
    }
    return nums.size();
}

void Remove::display(vector<int> &nums, int val)
{
    cout << endl
         << "calculation done!" << endl
         << endl;
    cout << "the number of different numbers: " << RemoveElement(nums, val) << endl;
    cout << "the vector is below:" << endl;
    for (vector<int>::iterator it = nums.begin(); it != nums.end(); it++)
    {
        cout << *it << " ";
    }
}

ostream &operator<<(ostream &output, vector<int> &nums)
{
    output << "the vector is below:" << endl;
    for (vector<int>::iterator it = nums.begin(); it != nums.end(); it++)
    {
        output << *it << " ";
    }
    // for (int i = 0; i < nums.size(); i++)
    // {
    //     output << nums.at(i) << " ";
    // }
    return output;
}

Remove::~Remove()
{
}
