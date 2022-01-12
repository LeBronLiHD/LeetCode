#include "merge.h"

int main()
{
    // [[-1,1],[-3,1,4],[-2,-1,0,2]]
    ListNode Two(1), One(-1, &Two);
    ListNode ThreeA(4), TwoA(1, &ThreeA), OneA(-3, &TwoA);
    ListNode FourAA(2), ThreeAA(0, &FourAA), TwoAA(-1, &ThreeAA), OneAA(-2, &TwoAA);
    vector<ListNode *> lists;
    lists.push_back(&One);
    lists.push_back(&OneA);
    lists.push_back(&OneAA);
    vector<ListNode *> listsEmpty;
    listsEmpty.push_back(NULL);
    listsEmpty.push_back(NULL);
    listsEmpty.push_back(NULL);

    merge Obj;
    // Obj.printLists(lists);
    Obj.printAns(Obj.mergeKLists(lists));
    return 0;
}