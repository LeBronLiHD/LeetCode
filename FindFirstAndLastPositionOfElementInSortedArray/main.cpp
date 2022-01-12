#include "FirstAndLast.h"

int main()
{
    FirstAndLast One({5, 7, 7, 8, 8, 10}, 8);
    FirstAndLast Two({5, 7, 7, 8, 8, 10}, 6);
    FirstAndLast Thr({}, 99);
    FirstAndLast Fou({99}, 99);
    One.printAns(One.searchRange());
    Two.printAns(Two.searchRange());
    Thr.printAns(Thr.searchRange());
    Fou.printAns(Fou.searchRange());
    return 0;
}