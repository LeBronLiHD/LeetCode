#include <vector>
#define MIN(a, b) (a > b) ? b : a

template <class vector>

class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        // 2020.12.17 模电呵呵呵
        int size = height.size();
        int contain = 0, temp;
        int i, j;
        for (i = 0; i < size; i++)
        {
            for (j = i + 1; j < size; j++)
            {
                temp = (j - i) * MIN(height.at(i), height.at(j));
                contain = (contain > temp) ? contain : temp;
            }
        }
        return contain;
    }
    Solution() {Nothing = 0;}

private:
    int Nothing;
};