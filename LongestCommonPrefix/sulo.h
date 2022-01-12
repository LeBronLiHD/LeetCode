#include <string>
#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        string res = "", temp;
        if (strs.size() == 0)
            return res;
        int size = strs.at(0).size(), flag = 1;
        for (int i = 0; i < strs.size(); i++)
            size = (size > strs.at(i).size()) ? strs.at(i).size() : size;
        if (size == 0)
            return res;

        while (res.size() < size && flag)
        {
            temp.assign(strs.at(0), res.size(), 1);
            for (int i = 1; i < strs.size(); i++)
                if (temp.compare(0, 1, strs.at(i), res.size(), 1) != 0)
                {
                    flag = 0;
                    break;
                }
            if (flag)
                res.append(temp);
        }

        return res;
    }
};