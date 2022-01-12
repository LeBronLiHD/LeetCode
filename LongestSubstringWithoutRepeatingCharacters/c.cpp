#include <iostream>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <unordered_map>
using namespace std;

int lengthOfLongestSubstring(char *s)
{
    int ans = 0, a = 0, t = 0;
    if (strlen(s) == 0)
        return 0;
    char temp;
    unordered_map<char, int> mys;
    for (int i = 0; s[i] != '\0'; i++)
    {
        for (int j = i; s[j] != '\0'; j++)
        {
            temp = s[j];
            if (mys.empty())
            {
                mys.insert(make_pair(temp, 0));
                t++;
            }
            else if (mys.find(temp) == mys.end())
            {
                mys.insert(make_pair(temp, 0));
                t++;
            }
            else
            {
                break;
            }
        }
        a = (a > t) ? a : t;
        ans = (a > ans) ? a : ans;
        t = 0;
        a = 0;
        mys.clear();
    }
    return ans;
}

int main()
{
    char a[50000];
    cout << endl
         << "Input a String Please: ";
    cin >> a;
    cout << endl;
    cout << "Your Input: " << a << endl
         << endl;
    int ans = lengthOfLongestSubstring(a);
    cout << "Longest Substring Without Repeating Characters is: " << ans << endl
         << endl;
    return 0;
}