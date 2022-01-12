#include "Rotation.h"

int main()
{
    Rotation One({4, 5, 6, 7, 0, 1, 2}, 0);
    Rotation Two({4, 5, 6, 7, 0, 1, 2}, 3);
    Rotation Thr({1}, 0);
    cout << "calculation done!" << endl;
    cout << "One.search() = " << One.search() << endl;
    cout << "Two.search() = " << Two.search() << endl;
    cout << "Thr.search() = " << Thr.search() << endl;
    return 0;
}