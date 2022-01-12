#include "Swap.h"

int main()
{
    ListNode One(1),
        Two(2, &One),
        Three(3, &Two),
        Four(4, &Three),
        Five(5, &Four);
    Swap Obj;
    // Obj.printVector(Obj.swapPairs(&Two));
    // Obj.printVector(Obj.swapPairs(&Three));
    Obj.printVector(Obj.swapPairs(&Five));
    // Obj.printVector(Obj.swapPairs(&Four));
    return 0;
}