#include <iostream>
#include <stdlib.h>
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
    ListNode *removeNthFromEnd(ListNode *head, int n);
};

Solution::Solution(/* args */)
{
    cout << "constructor called" << endl;
}

Solution::~Solution()
{
    cout << "destructor called" << endl;
}

ListNode *Solution::removeNthFromEnd(ListNode *head, int n)
{
    ListNode *Dummy, *first = head;
    Dummy = (ListNode*)malloc(sizeof(ListNode));
    Dummy->next = head;
    int length = 0;
    while (first != NULL)
    {
        length++;
        first = first->next;
    }

    int index = length - n - 1;
    first = Dummy;
    while (index > 0)
    {
        index--;
        first = first->next;
    }
    first->next = first->next->next;
    return Dummy->next;
}