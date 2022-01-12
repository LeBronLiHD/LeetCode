#include <iostream>
#include <stack>
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

// static ListNode *LHD = new ListNode(99);

class Reverse
{
private:
public:
    Reverse();
    ~Reverse();
    ListNode *reverseKGroup(ListNode *head, int k);
    ListNode *reverseList(ListNode *head, ListNode *terminal = NULL);
    void printAns(ListNode *ans);
};

Reverse::Reverse()
{
    cout << "constructor called" << endl;
}

ListNode *Reverse::reverseKGroup(ListNode *head, int k)
{
    if (k == 1)
        return head;
    ListNode *headAno = head;
    int length;
    for (length = 0; headAno; length++)
    {
        headAno = headAno->next;
    }
    if (length < k)
        return head;
    // main program is below
    stack<ListNode *> departures;
    ListNode *terminal, *cur = head;
    int index = 0;
    while (true)
    {
        if (index % k == 0)
        {
            if ((length - index) >= k)
                departures.push(cur);
            else
            {
                terminal = cur;
                break;
            }
        }
        if ((index + 1) % k == 0)
        {
            if (!cur->next)
            {
                terminal = NULL;
                break;
            }
            head = cur->next;
            cur->next = NULL;
            cur = head;
        }
        else
            cur = cur->next;
        index++;
    }
    while (!departures.empty())
    {
        terminal = reverseList(departures.top(), terminal);
        departures.pop();
    }
    return terminal;
}

ListNode *Reverse::reverseList(ListNode *head, ListNode *terminal)
{
    ListNode *cur = head,
             *tail = head,
             *curPost = cur->next;
    while (true)
    {
        cur->next = terminal;
        terminal = cur; // refresh the terminal
        cur = curPost;
        if (!cur->next)
        {
            head = cur;
            cur->next = terminal;
            break;
        }
        else
            curPost = cur->next;
    }
    return head;
}

void Reverse::printAns(ListNode *ans)
{
    cout << endl
         << "calculation done!" << endl
         << "the result is below:" << endl;
    while (ans->next)
    {
        cout << " " << ans->val << " ->";
        ans = ans->next;
    }
    cout << " " << ans->val << endl
         << endl;
}

Reverse::~Reverse()
{
    cout << "destructor called" << endl;
}
