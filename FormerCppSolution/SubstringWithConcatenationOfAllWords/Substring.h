#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Substring
{
private:
    string s;
    vector<string> words;

public:
    Substring(string str, vector<string> wor);
    ~Substring();
    vector<int> findSubstring();
    int length();
    int minLength();
    bool anyOrder(string part, vector<string> wordsElement);
    void display(vector<int> &ans);
};

Substring::Substring(string str, vector<string> wor) : s(str), words(wor)
{
}

vector<int> Substring::findSubstring()
{
    // 176 / 176 test cases passed, but took too long.
    int totalLength = length();
    // int step = minLength();
    int size = s.length();
    vector<int> ans;
    vector<string> temp;
    string part;
    for (int i = 0; i < size; i++)
    {
        part.assign(s, i, totalLength);
        if (totalLength > part.size())
            break;
        temp = words;
        if (anyOrder(part, temp))
            ans.push_back(i);
    }
    return ans;
}

int Substring::length()
{
    int ans = 0;
    for (vector<string>::iterator it = words.begin(); it != words.end(); it++)
    {
        ans += (*it).length();
    }
    return ans;
}

int Substring::minLength()
{
    int ans;
    for (vector<string>::iterator it = words.begin(); it != words.end(); it++)
    {
        ans = (ans <= (*it).length()) ? ans : (*it).length();
    }
    return ans;
}

bool Substring::anyOrder(string part, vector<string> wordsElement)
{
    int size = wordsElement.size();
    int total = part.size();
    int flag = 0;
    while (!part.empty())
    {
        flag = 0;
        for (vector<string>::iterator it = wordsElement.begin(); it != wordsElement.end(); it++)
        {
            if (0 == part.compare(0, (*it).length(), (*it)))
            {
                flag = 1;
                total = total - (*it).length();
                part.assign(part, (*it).length(), total);
                wordsElement.erase(it);
                it--;
            }
        }
        if (!flag)
            return false;
    }
    return true;
}

void Substring::display(vector<int> &ans)
{
    cout << "calculation done!" << endl;
    cout << "the result is below:" << endl;
    if (ans.empty())
    {
        cout << "NULL" << endl;
        return;
    }
    int size = ans.size();
    cout << ans.at(0) << " ";
    for (int i = 1; i < size; i++)
    {
        cout << "-> " << ans.at(i) << " ";
    }
    cout << endl;
    return;
}

Substring::~Substring()
{
}
