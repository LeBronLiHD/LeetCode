#include <iostream>
// #include <stdlib.h>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
};

class Solution
{
private:
    /* data */
public:
    Solution(/* args */);
    ~Solution();
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2);
};

Solution::Solution(/* args */)
{
    cout << "constructor called" << endl;
}

Solution::~Solution()
{
    cout << "destructor called" << endl;
}

ListNode *Solution::mergeTwoLists(ListNode *l1, ListNode *l2)
{
    ListNode *res = NULL, *temp, *cur;
    while (l1 != NULL && l2 != NULL)
    {
        temp = new ListNode;
        // temp->val = (l1->val > l2->val) ? l2->val : l1->val;
        if (l1->val > l2->val)
        {
            temp->val = l2->val;
            l2 = l2->next;
        }
        else
        {
            temp->val = l1->val;
            l1 = l1->next;
        }

        if (res == NULL)
        {
            res = temp;
            cur = temp;
            temp->next = NULL;
        }
        else
        {
            cur->next = temp;
            temp->next = NULL;
            cur = temp;
        }
    }

    if (l1 != NULL)
    {
        if (res == NULL)
        {
            res = l1;
            cur = l1;
        }
        else
        {
            cur->next = l1;
        }
        while (l1 != NULL)
        {
            if (l1->next == NULL)
            {
                cur = l1;
            }
            l1 = l1->next;
        }
    }
    else if (l2 != NULL)
    {
        if (res == NULL)
        {
            res = l2;
            cur = l2;
        }
        else
        {
            cur->next = l2;
        }
        while (l2 != NULL)
        {
            if (l2->next == NULL)
            {
                cur = l2;
            }
            l2 = l2->next;
        }
    }

    return res;
}