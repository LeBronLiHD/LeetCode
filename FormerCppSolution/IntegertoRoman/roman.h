#include <string>
using namespace std;

// template<>
string sym[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
int val[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

class Solution
{
public:
    string intToRoman(int num)
    {
        string res = "";
        int res_int = 0;
        int i = 0, ori = num;
        while (res_int < ori)
        {
            while (val[i] > num)
            {
                i++;
            }
            res_int += val[i];
            res.append(sym[i]);
            num -= val[i];
            i = 0;
        }
        return res;
    }
    // Solution();
private:
};