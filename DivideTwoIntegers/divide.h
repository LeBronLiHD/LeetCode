#include <iostream>
#include <math.h>
using namespace std;

const long signed int MAX = pow(2, 31) - 1;
const long signed int MIN = pow(-2, 31);

class divide
{
private:
    long signed int dividend;
    long signed int divisor;

public:
    divide(long signed int a, long signed int b);
    ~divide();
    long signed int divideFunction();
};

divide::divide(long signed int a, long signed int b) : dividend(abs(a)), divisor(abs(b))
{
    cout << "constructor called" << endl;
}

long signed int divide::divideFunction()
{
    // range: [−2^31,  2^31 − 1].
    // returns 2^31 − 1 when the division result overflows.
    if ((dividend / divisor) > MAX)
        return MAX;
    else if ((dividend / divisor) < MIN)
        return MIN;
    else
        return dividend / divisor;
}

divide::~divide()
{
    cout << "destructor called" << endl;
}
