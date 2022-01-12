#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
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
    void display(vector<int> &ans);
};

Substring::Substring(string str, vector<string> wor) : s(str), words(wor)
{
}

vector<int> Substring::findSubstring()
{
    unordered_map<string, int> counts;
    for (string word : words)
    {
        counts[word]++;
    }
    int size = s.length();
    int num = words.size();
    int len = words.at(0).length(); // every word is same in length
    vector<int> ans;
    // we check for every possible position of i. 
    // once we meet an unexpected word or the times of some word is larger than its expected times, we stop the check. 
    // if we finish the check successfully, push i to the result ans.
    for (int i = 0; i < size - num * len + 1; i++)
    {
        unordered_map<string, int> seen;
        int j = 0;
        for (; j < num; j++)
        {
            string word = s.substr(i + j * len, len);
            if (counts.find(word) != counts.end())
            {
                seen[word]++;
                if (seen[word] > counts[word])
                    break;
            }
            else
                break;
        }
        if (j == num)
        {
            ans.push_back(i);
        }
    }
    return ans;
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
