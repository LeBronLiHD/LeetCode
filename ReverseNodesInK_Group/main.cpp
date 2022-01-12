#include "reverse.h"

int main()
{
    ListNode One(1),
        Two(2, &One),
        Three(3, &Two),
        Four(4, &Three),
        Five(5, &Four),
        Six(6, &Five),
        Seven(7, &Six),
        Eight(8, &Seven),
        Nine(9, &Eight);
    int k;
    cout << endl
         << "Input the size of Reverse Group: ";
    cin >> k;
    cout << endl;
    Reverse Obj;
    Obj.printAns(Obj.reverseKGroup(&Nine, k));
    return 0;
}