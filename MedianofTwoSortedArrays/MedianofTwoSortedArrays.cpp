#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

bool up(int a, int b)
{
    return a < b;
}

double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2)
{
    int size1;
    int size2 = nums2.size();
    double sum = 0, ans;
    for (int i = 0; i < size2; i++)
        nums1.push_back(nums2.at(i));
    sort(nums1.begin(), nums1.end(), up);
    size1 = nums1.size();
    cout << "after sorting: ";
    for (int i = 0; i < size1; i++)
        cout << nums1[i] << " ";
    cout << endl
         << "size of nums1 is: " << size1
         << endl;

    if (size1 % 2 == 1)
    {
        ans = (double)nums1[(size1 - 1) / 2];
        return ans;
    }
    else if (size1 != 0)
    {
        ans = ((double)nums1[size1 / 2 - 1] + (double)nums1[size1 / 2]) / 2.0;
        return ans;
    }
    else
        return 0;
}

int main()
{
    cout << fixed << setprecision(6);
    vector<int> num1, num2;
    int n1, n2, n;
    cout << endl
         << "the length of num1: ";
    cin >> n1;
    cout << "the length of num2: ";
    cin >> n2;
    cout << endl;
    for (int i = 0; i < n1; i++)
    {
        cout << "the " << i + 1 << " element of nums1: ";
        cin >> n;
        num1.push_back(n);
    }
    cout << endl;
    for (int i = 0; i < n2; i++)
    {
        cout << "the " << i + 1 << " element of nums2: ";
        cin >> n;
        num2.push_back(n);
    }
    cout << endl;
    double ans = findMedianSortedArrays(num1, num2);
    cout << endl
         << "the answer is: " << ans << endl;
}