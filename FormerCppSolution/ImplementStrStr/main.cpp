#include "StrStr.h"

int main()
{
    string haystack = "hello", needle = "ll";
    // cout << haystack.compare(2, 2, needle) << endl;
    StrStr Obj;
    // cout << "the result is: " << Obj.strStrFunction(haystack, needle) << endl;
    switch (Obj.strStrFunction(haystack, needle))
    {
    case -1:
        cout << "needle IS NOT part of haystack" << endl;
        break;
    case 0:
        cout << "needle is EMPTY or at the very beginning of haystack" << endl;
        break;
    default:
        cout << "needle IS part of haystack" << endl;
        break;
    }
    return 0;
}