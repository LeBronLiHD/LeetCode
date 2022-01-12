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
    ListNode *generator(vector<int> minSet);
    void printLists(vector<ListNode *> lists);
    void printAns(ListNode *ans);
};

merge::merge(/* args */)
{
    cout << "constructor called" << endl;
}

ListNode *merge::mergeKLists(vector<ListNode *> &lists)
{
    if (lists.empty())
        return NULL;
    vector<ListNode *>::iterator it;
    int flag = 0;
    for (it = lists.begin(); it != lists.end();)
    {
        if (*it)
        {
            flag = 1;
            it++;
        }
        else
            lists.erase(it);
    }
    if (!flag)
        return NULL;

    vector<int> minSet;
    int index;
    int finalIndex;
    while (!lists.empty())
    {
        printLists(lists);
        ListNode *min = (*lists.begin());
        index = 0;
        finalIndex = 0;
        for (it = lists.begin(), it++; it != lists.end(); it++)
        {
            index++;
            if (min->val > (*it)->val)
            {
                min = (*it);
                finalIndex += index;
                index = 0;
            }
        }
        it = lists.begin();
        for (int i = 0; i < finalIndex; i++)
            it++;
        (*it) = (*it)->next;
        if (!(*it))
            lists.erase(it);

        int minValue = min->val;
        cout << "current min value is: " << minValue << endl;
        minSet.push_back(minValue);
    }
    return generator(minSet);
}

ListNode *merge::generator(vector<int> minSet)
{
    ListNode *ans = NULL;
    ListNode *cur = NULL;
    int size = minSet.size();
    for (int i = 0; i < size; i++)
    {
        ListNode *temp = new ListNode;
        temp->val = minSet.at(i);
        temp->next = NULL;
        if (!ans)
        {
            cur = temp;
            ans = cur;
        }
        else
        {
            cur->next = temp;
            cur = cur->next;
        }
    }
    return ans;
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
