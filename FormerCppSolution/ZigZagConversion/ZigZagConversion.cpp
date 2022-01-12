#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
// namespace std

string convert(string s, int numRows)
{
    if (numRows == 1)
        return s;
    int curRows = 0, size = min(numRows, int(s.size()));
    vector<string> rows(size);
    bool down = false;

    for (char c : s)
    {
        rows.at(curRows) += c;
        if (curRows == 0 || curRows == numRows - 1)
            down = !down;
        curRows += down ? 1 : -1;
    }

    string ans;
    for (string row : rows)
        ans += row;
    return ans;
}

int main()
{
    cout << endl
         << "Input a string please: ";
    string s, ans;
    getline(cin, s);

    int n;
    cout << endl
         << "Input the row number: ";
    cin >> n;
    ans = convert(s, n);
    cout << endl
         << "The answer is: " << endl
         << ans << endl;
    return 0;
}