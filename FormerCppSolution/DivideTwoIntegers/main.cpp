#include "divide.h"

int main()
{
    divide ObjOne(-2147483648, -1), ObjTwo(10, 3);
    cout << "the result is: " << ObjOne.divideFunction() << endl;
    cout << "the result is: " << ObjTwo.divideFunction() << endl;
    return 0;
}