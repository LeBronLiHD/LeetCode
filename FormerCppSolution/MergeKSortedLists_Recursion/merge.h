#include <iostream>
#include <vector>
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

class merge
{
private:
public:
    merge();
    ~merge();
    ListNode *mergeKLists(vector<ListNode *> &lists);
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2);
    void printLists(vector<ListNode *> lists);
    void printAns(ListNode *ans);
};

merge::merge(/* args */)
{
    cout << "constructor called" << endl;
}

ListNode *merge::mergeKLists(vector<ListNode *> &lists)
{
    if(lists.empty())
        return NULL;
    while(lists.size() > 1)
    {
        lists.push_back(mergeTwoLists(lists.at(0), lists.at(1)));
        lists.erase(lists.begin());
        lists.erase(lists.begin());
    }
    return lists.front(); // equal to lists.at(0)
}

ListNode *merge::mergeTwoLists(ListNode *l1, ListNode *l2)
{
    if (!l1)
    {
        return l2;
    }
    if (!l2)
    {
        return l1;
    }
    if (l1->val <= l2->val)
    {
        l1->next = mergeTwoLists(l1->next, l2);
        return l1;
    }
    else
    {
        l2->next = mergeTwoLists(l1, l2->next);
        return l2;
    }
}

void merge::printLists(vector<ListNode *> listsPrint)
{
    cout << endl
         << "the Lists are below: " << endl;
    int size = listsPrint.size();
    for (int i = 0; i < size; i++)
    {
        ListNode *element = listsPrint.at(i);
        while (element->next)
        {
            cout << " " << element->val << " ->";
            element = element->next;
        }
        cout << " " << element->val << endl;
    }
}

void merge::printAns(ListNode *ans)
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

merge::~merge()
{
    cout << "destructor called" << endl;
}