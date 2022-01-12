#include <iostream>
#include <string>
using namespace std;

class StrStr
{
private:
public:
    StrStr();
    ~StrStr();
    int strStrFunction(string haystack, string needle);
};

StrStr::StrStr()
{
    cout << "constructor called" << endl;
}

int StrStr::strStrFunction(string haystack, string needle)
{
    if (needle.empty())
        return 0;
    int size = needle.size();
    int deltaSize = haystack.length() - size;
    for (int i = 0; i <= deltaSize; i++)
    {
        // start at index i and compare with size number of elements after index i
        if (!haystack.compare(i, size, needle))
            return i;
    }
    return -1;
}

StrStr::~StrStr()
{
    cout << "destructor called" << endl;
}
