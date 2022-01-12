#include <iostream>
#include <stdlib.h>
using namespace std;

struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode *reverse(struct ListNode *l)
{
    int cnt = 0;
    struct ListNode *a = l;
    struct ListNode *ans = NULL;
    struct ListNode *temp, *t;
    while (a != NULL)
    {
        cnt++;
        a = a->next;
    }
    int rev[100];
    for (int i = 0; i < cnt; i++)
    {
        rev[i] = l->val;
        l = l->next;
    }
    for (int i = cnt - 1; i >= 0; i--)
    {
        t = (struct ListNode *)malloc(sizeof(struct ListNode));
        t->val = rev[i];
        if (ans == NULL)
        {
            ans = t;
            temp = t;
            ans->next = NULL;
            temp->next = NULL;
        }
        else
        {
            temp->next = t;
            temp = t;
            temp->next = NULL;
        }
    }
    return ans;
}

struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2)
{
    struct ListNode *ans = NULL;
    struct ListNode *t, *temp;
    int flag = 0, tmp;
    while (l1 != NULL && l2 != NULL)
    {
        t = (struct ListNode *)malloc(sizeof(struct ListNode));
        tmp = l1->val + l2->val;
        if (flag)
        {
            tmp++;
            flag = 0;
        }
        if (tmp >= 10)
        {
            t->val = tmp % 10;
            flag = 1;
        }
        else
        {
            t->val = tmp;
        }
        if (ans == NULL)
        {
            ans = t;
            temp = t;
            ans->next = NULL;
            temp->next = NULL;
        }
        else
        {
            temp->next = t;
            temp = t;
            temp->next = NULL;
        }
        l1 = l1->next;
        l2 = l2->next;
    }
    while (l1 != NULL)
    {
        t = (struct ListNode *)malloc(sizeof(struct ListNode));
        tmp = l1->val;
        if (flag)
        {
            tmp++;
            flag = 0;
        }
        if (tmp >= 10)
        {
            t->val = tmp % 10;
            flag = 1;
        }
        else
        {
            t->val = tmp;
        }
        temp->next = t;
        temp = t;
        temp->next = NULL;
        l1 = l1->next;
    }
    while (l2 != NULL)
    {
        t = (struct ListNode *)malloc(sizeof(struct ListNode));
        tmp = l2->val;
        if (flag)
        {
            tmp++;
            flag = 0;
        }
        if (tmp >= 10)
        {
            t->val = tmp % 10;
            flag = 1;
        }
        else
        {
            t->val = tmp;
        }
        temp->next = t;
        temp = t;
        temp->next = NULL;
        l2 = l2->next;
    }
    if (flag)
    {
        t = (struct ListNode *)malloc(sizeof(struct ListNode));
        t->val = 1;
        temp->next = t;
        temp = t;
        temp->next = NULL;
        return ans /*reverse(ans)*/;
    }
    else
        return ans;
}

int main()
{
    struct ListNode *l1 = NULL, *l2 = NULL, *temp;
    int n, v;
    cout << endl
         << "START" << endl
         << endl
         << "for l1:";
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cout << "INTER the " << i + 1 << " element ->";
        cin >> v;
        struct ListNode *t = (struct ListNode *)malloc(sizeof(struct ListNode));
        t->val = v;
        if (l1 == NULL)
        {
            l1 = t;
            temp = t;
            l1->next = NULL;
            temp->next = NULL;
        }
        else
        {
            temp->next = t;
            temp = t;
            temp->next = NULL;
        }
    }
    cout << "for l2:";
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cout << "INTER the " << i + 1 << " element ->";
        cin >> v;
        struct ListNode *t = (struct ListNode *)malloc(sizeof(struct ListNode));
        t->val = v;
        if (l2 == NULL)
        {
            l2 = t;
            temp = t;
            l2->next = NULL;
            temp->next = NULL;
        }
        else
        {
            temp->next = t;
            temp = t;
            temp->next = NULL;
        }
    }
    cout << endl;
    struct ListNode *ans = addTwoNumbers(l1, l2);
    while (ans != NULL)
    {
        cout << ans->val;
        ans = ans->next;
    }
    return 0;
}