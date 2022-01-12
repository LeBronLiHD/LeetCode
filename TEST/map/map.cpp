#include <iostream>
#include <string>
#include <map>
#include <unordered_map>
using namespace std;

// M.size()
// M.clear()
// M.begin() & M.end()
// M.insert(pair<int, string>(index, "String"))
// M.find(value)

int main()
{
    cout << "Map" << endl;
    map<int, string> M;
    M[1] = "Tom";
    M[2] = "Max";
    M[3] = "Mark";
    M[4] = "John";
    M[5] = "Pat";
    cout << "M[4] = " << M[4] << endl; // M[4] = John
    M.insert(pair<int, string>(6, "LHD"));
    for (map<int, string>::iterator it = M.begin(); it != M.end(); it++)
        cout << it->first << " -> " << it->second << endl;
    // 1 -> Tom
    // 2 -> Max
    // ...
    // 6 -> LHD
    map<int, string>::iterator it = M.find(3);
    cout << "Find M[3] = " << it->second << endl;
    M.erase(it);
    for (map<int, string>::iterator it = M.begin(); it != M.end(); it++)
        cout << it->first << " -> " << it->second << endl;

    cout << endl
         << "unordered_map" << endl;
    unordered_map<char, int> U;
    return 0;
}