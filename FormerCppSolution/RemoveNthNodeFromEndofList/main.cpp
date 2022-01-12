#include "Solution.h"

void print(ListNode *head)
{
    ListNode *first = head;
    cout << endl
         << "[";
    while (first != NULL)
    {
        cout << " " << first->val << " ";
        first = first->next;
    }
    cout << "]" << endl;
}

int main()
{
    ListNode *head, *cur;
    for (int i = 0; i < 5; i++)
    {
        ListNode *temp = (ListNode *)malloc(sizeof(ListNode));
        if (i == 0)
        {
            head = temp;
            cur = head;
        }
        else
        {
            cur->next = temp;
            cur = cur->next;
        }

        temp->next = NULL;
        temp->val = i * i + 9;
    }
    print(head);
    Solution Obj;
    Obj.removeNthFromEnd(head, 2);
    print(head);
    return 0;
}
/*
Runtime: 0 ms, faster than 100.00% of C++ online submissions for Remove Nth Node From End of List.
Memory Usage: 11.2 MB, less than 51.89% of C++ online submissions for Remove Nth Node From End of List.
*/