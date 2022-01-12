#include <iostream>
#include <vector>
using namespace std;

class Duplicate
{
private:
public:
    Duplicate();
    ~Duplicate();
    int removeDuplicates(vector<int> &nums);
    void display(vector<int> &nums);
    friend ostream &operator<<(ostream &output, vector<int> &nums);
};

Duplicate::Duplicate()
{
}

int Duplicate::removeDuplicates(vector<int> &nums)
{
    if (nums.empty())
        return 0;
    else if (nums.size() == 1)
        return 1;
    int preValue = nums.at(0), count = 1;
    vector<int>::iterator it = nums.begin();
    it++;
    for (; it != nums.end(); it++)
    {
        if (preValue == (*it))
        {
            if (it == nums.end())
            {
                nums.erase(it);
                count--;
                return count;
            }
            else
            {
                nums.erase(it);
                count--;
                it--;
            }
        }
        preValue = (*it);
        count++;
    }
    return count;
}

void Duplicate::display(vector<int> &nums)
{
    cout << endl
         << "calculation done!" << endl
         << endl;
    cout << "the number of different numbers: " << removeDuplicates(nums) << endl;
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

Duplicate::~Duplicate()
{
}
