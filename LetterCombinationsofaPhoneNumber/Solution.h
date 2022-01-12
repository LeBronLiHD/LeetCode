#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

class Solution
{
private:
    /* data */
public:
    Solution(/* args */);
    vector<string> letterCombinations(string digits);
    void combinations(string digits, string &combination, unordered_map<char, string> &numToString, int index, vector<string> &res);
    ~Solution();
};

Solution::Solution(/* args */)
{
    cout << "constructor called" << endl;
}

vector<string> Solution::letterCombinations(string digits)
{
    if (digits.empty())
        return {};

    unordered_map<char, string> numToString;
    numToString.insert(make_pair('2', "abc"));
    numToString.insert(make_pair('3', "def"));
    numToString.insert(make_pair('4', "ghi"));
    numToString.insert(make_pair('5', "jkl"));
    numToString.insert(make_pair('6', "mno"));
    numToString.insert(make_pair('7', "pqrs"));
    numToString.insert(make_pair('8', "tuv"));
    numToString.insert(make_pair('9', "wxyz"));

    int n = digits.length();
    int index = 0;
    string combination(n, ' ');
    vector<string> result;
    combinations(digits, combination, numToString, index, result);
    return result;
}

void Solution::combinations(string digits, string &combination, unordered_map<char, string> &numToString, int index, vector<string> &res)
{
    if (index == digits.length())
    {
        res.push_back(combination);
        return;
    }

    for (char c : numToString.at(digits.at(index)))
    {
        combination.at(index) = c;
        combinations(digits, combination, numToString, ++index, res);
        index--;
    }
}

Solution::~Solution()
{
    cout << "deconstructor called" << endl;
}
