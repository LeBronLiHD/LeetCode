#include <iostream>
using namespace std;

// Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Swap
{
private:
public:
    Swap();
    ~Swap();
    ListNode *swapPairs(ListNode *head);
    void printVector(ListNode *head);
};

Swap::Swap()
{
}

ListNode *Swap::swapPairs(ListNode *head)
{
    if (!head || !head->next)
        return head;
    ListNode *cur = head,
             *curPost = head->next,
             *curPre = NULL,
             *newHead = head->next;
    if (!curPost->next)
    {
        curPost->next = cur;
        cur->next = NULL;
        return curPost;
    }
    while (curPost)
    {
        if (!curPost->next)
        {
            curPre->next = curPost;
            curPost->next = cur;
            cur->next = NULL;
            break;
        }
        else if (!curPre)
        {
            curPre = cur; // initialize
            cur->next = curPost->next;
            curPost->next = cur;
            cur = cur->next;
            curPost = cur->next;
        }
        else
        {
            curPre->next = curPost;
            cur->next = curPost->next;
            curPost->next = cur;
            curPre = cur; // renew
            cur = curPre->next;
            curPost = cur->next;
        }
    }
    return newHead;
}

void Swap::printVector(ListNode *head)
{
    if (!head)
    {
        cout << "NULL" << endl;
        return;
    }
    while (head->next)
    {
        cout << " " << head->val << " ->";
        head = head->next;
    }
    cout << " " << head->val << endl;
    return;
}

Swap::~Swap()
{
}