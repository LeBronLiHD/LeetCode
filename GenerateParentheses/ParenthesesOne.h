#ifndef PARENTHESESONE_H
#define PARENTHESESONE_H

#include <vector>
#include <string>
#include <iostream>
using namespace std;

class ParenthesesOne
{
private:
    /* data */
public:
    ParenthesesOne(/* args */);
    ~ParenthesesOne();
    vector<string> generateParenthesis(int n);
    vector<string> generateOriginal(int n);
    bool valid(string temp);
};

ParenthesesOne::ParenthesesOne(/* args */)
{
}

ParenthesesOne::~ParenthesesOne()
{
}

vector<string> ParenthesesOne::generateParenthesis(int n)
{
    vector<string> ori = generateOriginal(2 * n);
    vector<string> ans;
    for (int i = ori.size() / 2 - 1; i < ori.size(); i++)
    {
        if (valid(ori.at(i)))
            ans.push_back(ori.at(i));
    }
    return ans;
}

bool ParenthesesOne::valid(string temp)
{
    int count;
    for (int i = 0; i < temp.length(); i++)
    {
        if (temp.at(i) == '(')
            count++;
        else
            count--;
        if (count < 0)
            return false;
    }
    if (count == 0)
        return true;
    else
        return false;
}

vector<string> ParenthesesOne::generateOriginal(int n)
{
    if(n == 1)
        return {"(", ")"};
    vector<string> ans = generateOriginal(n - 1);
    int size = ans.size();
    for (int i = 0; i < size; i++)
        ans.push_back(ans.at(i));
    for (int i = 0; i < ans.size(); i++)
    {
        if (i < size)
            ans.at(i).append("(");
        else
            ans.at(i).append(")");
    }
    return ans;
}

#endif //PARENTHESESONE_H
