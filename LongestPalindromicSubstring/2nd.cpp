#include <iostream>
#include <cstring>
#include <string>
#include <map>
using namespace std;

int judge(string s)
{
    int size = s.size();
    int end = size / 2, i = 0;
    while (i <= end)
    {
        if (s.at(i) != s.at(size - i - 1))
            return 0;
        i++;
    }
    return 1;
}

string reverse(string s)
{
    string ans = s;
    int i = 0, size = s.size();
    while (i < size)
    {
        ans.at(i) = s.at(size - i - 1);
        i++;
    }
    return ans;
}

string compareUnit(string s, string rs)
{
    int max = 0, temp = 0;
    map<int, int> len;
    int size = rs.size();
    for (int i = 0; i < size; i++)
    {
        while (i < size && s.at(i) == rs.at(i))
        {
            i++;
            temp++;
        }
        if (temp > max &&judge(s.substr( i - temp, temp)))
        {
            max = temp;
            len.insert(make_pair(temp, i - temp));
        }
        temp = 0;
    }
    auto it = len.find(max);
    return s.substr(it->second, it->first);
}

string compare(string s, string rs)
{
    int max = 1, temp = 0, size = s.size();
    string m = s.substr(0, 1), t, change;
    s = s.insert(size - 1, s.substr(size - 1, 1), 0, 1);
    s.at(size) = '?';
    char tem;
    for (int i = 0; i <= size; i++)
    {
        t = compareUnit(s, rs);
        temp = t.size();
        if (temp > max)
        {
            max = temp;
            m = t;
        }
        tem = s.at(0);
        change = s.substr(1, size);
        s.insert(0, change, 0, size);
        s.at(size) = tem;
        s = s.erase(size + 1);
    }
    return m;
}

string longestPalindrome(string s)
{
    if(!s.size())
        return "";
    string rs = reverse(s);
    cout << "reverse output: " << rs << endl;
    return compare(s, rs);
}

int main()
{
    string s, ans;
    cout << endl
         << "Input the string you want to deal with: ";
    getline(cin, s);
    cout << endl
         << "You input: " << s << endl;
    ans = longestPalindrome(s);
    cout << "Longest Palindromic Substring is: " << ans << endl;
    return 0;
}