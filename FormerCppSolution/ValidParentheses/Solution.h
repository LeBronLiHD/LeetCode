#include <iostream>
#include <string>
#include <stack>
using namespace std;

class Solution
{
private:
    /* data */
public:
    Solution(/* args */);
    ~Solution();
    bool isValid(string s);
};

Solution::Solution(/* args */)
{
    cout << "Constructor Called" << endl;
}

Solution::~Solution()
{
    cout << "Destructor Called" << endl;
}

bool Solution::isValid(string s)
{
    int n = s.length();
    string::size_type idx;
    char temp;
    // string::size_type dix;
    string input = "([{)]}";
    string output = ")]}([{";
    string findIN = "";
    string findOUT = "";
    stack<char> sta;
    for (int i = 0; i < n; i++)
    {
        findIN = findIN + s.at(i);
        idx = input.find(findIN); // find char in INPUT
        if (sta.size())
            findOUT = findOUT + sta.top(); // find char in OUTPUT
        if (sta.empty() || output.find(findOUT) != idx || idx < input.find(")"))
        {
            sta.push(s.at(i));
        }
        else
        {
            sta.pop();
        }

        findIN.clear();
        findOUT.clear();
    }
    if (sta.size())
        return false;
    else
        return true;
}