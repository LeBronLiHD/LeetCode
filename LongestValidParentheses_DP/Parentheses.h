#include <iostream>
#include <iomanip>
#include <string>
#include <stack>
#include <vector>
using namespace std;

class Parentheses
{
private:
    string s;

public:
    Parentheses(string S);
    ~Parentheses();
    int longestValidParentheses();
    bool judgeValid(string &part);
};

Parentheses::Parentheses(string S) : s(S)
{
    cout << "constructor called" << endl;
}

int Parentheses::longestValidParentheses() // DP, very fast
{
    int stringSize = s.length();
    if (stringSize <= 1)
        return 0;
    int curMax = 0;
    vector<int> longest(stringSize, 0);
    for (int i = 1; i < stringSize; i++)
    {
        if (s.at(i) == ')' && i - longest.at(i - 1) - 1 >= 0 && s.at(i - longest.at(i - 1) - 1) == '(')
        {
            longest.at(i) = longest.at(i - 1) + 2 +
                            ((i - longest.at(i - 1) - 2 >= 0)
                                 ? longest.at(i - longest.at(i - 1) - 2)
                                 : 0);
            curMax = max(longest.at(i), curMax);
        }
        // ...MAXONE'('MAXTWO')'...
        // and longest.at(i) = MAXONE + MAXTWO + 2
    }
    return curMax;
}

bool Parentheses::judgeValid(string &part)
{
    int size = part.length();
    stack<char> leftStack;
    for (size_t i = 0; i < size; i++)
    {
        if (part.at(i) == '(')
        {
            leftStack.push(part.at(i));
        }
        else
        {
            if (leftStack.empty())
                return false;
            else
                leftStack.pop();
        }
    }
    if (leftStack.empty())
        return true;
    else
        return false;
}

Parentheses::~Parentheses()
{
    cout << "destructor called" << endl;
}
