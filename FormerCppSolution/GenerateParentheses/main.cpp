#include "ParenthesesOne.h"

int main()
{
    int n;
    cout << "Inter a number: ";
    cin >> n;
    ParenthesesOne Obj;
    vector<string> ans = Obj.generateParenthesis(n);
    cout << "[";
    for (int i = 0; i < ans.size(); i++)
    {
        cout << "\"" << ans.at(i) << "\"";
        if (i != ans.size() - 1)
            cout << ",";
    }
    cout << "]" << endl
         << "Total: " << ans.size() << endl;
    return 0;
}