#include "search.h"

int main()
{
    Search One({1, 3, 5, 6}, 5); // 2
    Search Two({1, 3, 5, 6}, 0); // 0
    Search Thr({1, 3, 5, 6}, 4); // 2
    Search Fou({1, 3, 5, 6}, 9); // 4
    Search Fiv({1, 3, 5, 6}, 2); // 1
    Search Six({1}, 1);          // 1
    cout << "calculation done!" << endl;
    cout << "One.searchInsert() = " << One.searchInsert() << endl;
    cout << "Two.searchInsert() = " << Two.searchInsert() << endl;
    cout << "Thr.searchInsert() = " << Thr.searchInsert() << endl;
    cout << "Fou.searchInsert() = " << Fou.searchInsert() << endl;
    cout << "Fiv.searchInsert() = " << Fiv.searchInsert() << endl;
    cout << "Six.searchInsert() = " << Six.searchInsert() << endl;
    return 0;
}