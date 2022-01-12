#include "Solution.h"

ListNode *Init(int a)
{
    ListNode *head, *temp, *cur;
    for (int i = 0; i < 5; i++)
    {
        temp = new ListNode;
        temp->val = i * 2 + a;
        temp->next = NULL;
        if (i == 0)
        {
            head = temp;
            cur = temp;
        }
        else
        {
            cur->next = temp;
            cur = temp;
        }
    }
    return head;
}

void print(ListNode *res)
{
    cout << endl
         << "[";
    while (res != NULL)
    {
        cout << " " << res->val << " ";
        res = res->next;
    }
    cout << "]" << endl;
}

int main()
{
    ListNode *liOne = Init(1);
    ListNode *liTwo = Init(2);
    Solution Obj;
    ListNode *res = Obj.mergeTwoLists(liOne, liTwo);
    print(res);
}
/*
Runtime: 8 ms, faster than 84.48% of C++ online submissions for Merge Two Sorted Lists.
Memory Usage: 15.4 MB, less than 13.15% of C++ online submissions for Merge Two Sorted Lists.
*/