#include "Rotation.h"

int main()
{
    Rotation One({4, 5, 6, 7, 0, 1, 2}, 0); // 4
    Rotation Two({4, 5, 6, 7, 0, 1, 2}, 3); // -1
    Rotation Thr({1, 3}, 1);                // 0
    Rotation Fou({3, 1}, 1);                // 1
    Rotation Fiv({3, 5, 1}, 5);             // 1
    cout << "calculation done!" << endl;
    cout << "One.search() = " << One.search() << endl;
    cout << "Two.search() = " << Two.search() << endl;
    cout << "Thr.search() = " << Thr.search() << endl;
    cout << "Fou.search() = " << Fou.search() << endl;
    cout << "Fiv.search() = " << Fiv.search() << endl;
    return 0;
}