#include <iostream>
#include <string>
#include <map>
#include <unordered_map>
using namespace std;

int main()
{
    unordered_map<string, double> constants;

    string pi = "PI";
    string root2 = "ROOT2";
    string e = "E";

    constants[pi] = 3.1416;
    constants[root2] = 1.414;
    //constants[e] = 2.718;

    constants.insert(make_pair(e,2.718));

    for(auto it = constants.begin(); it != constants.end(); it++)
        cout << "Key[" << it->first << "] is : " << it->second <<endl;
    
    string lambda = "LAMBDA";

    if(constants.find(lambda) == constants.end())
        cout << "Was not able to find: " << lambda << endl;
    return 0;
}