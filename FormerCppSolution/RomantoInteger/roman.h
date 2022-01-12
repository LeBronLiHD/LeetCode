#include <string>
#include <iostream>
using namespace std;

string sym[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
int val[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

class Solution
{
private:
    /* data */
public:
    Solution(/* args */);
    int romanToInt(string s);
    ~Solution();
};

Solution::Solution(/* args */)
{
    cout << "constructor called" << endl;
}

int Solution::romanToInt(string s)
{
    int res = 0;
    int size = s.size();
    int i, com, index = 0;
    while (size > 0)
        for (i = 0; i < 13; i++)
        {
            cout << "cur length = " << sym[i].size() << endl;
            com = sym[i].compare(0, sym[i].size(), s, index, sym[i].size());
            if (com == 0)
            {
                size -= sym[i].size();
                index += sym[i].size();
                res += val[i];
            }
        }
    return res;
}

Solution::~Solution()
{
    cout << "deconstructor called" << endl;
}
